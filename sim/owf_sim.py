"""Stress-test OWF v0.1 section 7 (hand-in to credit) with an agent-based model.

Each agent delivers true value over 52 weeks. A noisy judge places each
contribution against the reference set. We compare each group's share of
credit with its share of true value delivered: 1.0 is fair, >1 means the
group is gaining at others' expense.
"""
import random
import statistics

WEEKS = 52
STAGES = [(0, 2.0), (10, 1.5), (26, 1.2), (40, 1.0)]  # week stage starts, multiplier


def multiplier(week):
    m = STAGES[0][1]
    for start, mult in STAGES:
        if week >= start:
            m = mult
    return m


class Judge:
    def __init__(self, compression=0.85, noise=0.3, polish_bias=0.4,
                 length_norm=False, insider_lowball=0.0):
        self.compression = compression    # judges flatten big work (RetroPGF)
        self.noise = noise
        self.polish_bias = polish_bias
        self.length_norm = length_norm
        self.insider_lowball = insider_lowball

    def place(self, value, polished=False, newcomer=False):
        p = (value ** self.compression) * random.lognormvariate(0, self.noise)
        if polished:
            p *= 1 + (self.polish_bias * (0.25 if self.length_norm else 1))
        if newcomer:
            p *= 1 - self.insider_lowball
        return p


def gini(xs):
    xs = sorted(x for x in xs)
    n = len(xs)
    total = sum(xs)
    if total == 0:
        return 0
    cum = sum((i + 1) * x for i, x in enumerate(xs))
    return (2 * cum) / (n * total) - (n + 1) / n


def run(cfg, seed):
    random.seed(seed)
    judge = Judge(**cfg.get('judge', {}))
    bundle = cfg.get('bundle', True)
    catch = cfg.get('fraud_catch', 0.6)
    agents = []

    def add(kind, n, **kw):
        for i in range(n):
            agents.append(dict(kind=kind, id=f'{kind}{i}', credit=0.0, true=0.0, **kw))

    add('founder', 2, start=0, rate=0.9, size=40)
    add('honest', 20, start=0, rate=0.3, size=25, late=True)
    add('whale', 1, start=8, rate=1.0, size=30)
    for kind, n, kw in cfg.get('extra', []):
        add(kind, n, **kw)

    for a in agents:
        if a.get('late'):
            a['start'] = random.randint(4, 40)

    for week in range(WEEKS):
        mult = multiplier(week)
        for a in agents:
            if week < a['start'] or random.random() > a['rate']:
                continue
            v = random.lognormvariate(0, 0.8) * a['size'] / 1.4
            newcomer = a['kind'] != 'founder'
            k = a['kind']
            if k == 'splitter':
                a['true'] += v
                pieces = [v / a['k']] * a['k']
                spread = a.get('across_windows', False)
                if cfg.get('cumulative'):
                    # re-place the running total for this need, award the difference, never negative
                    done, awarded = 0.0, 0.0
                    for p in pieces:
                        done += p
                        whole = judge.place(done, newcomer=newcomer)
                        a['credit'] += max(0.0, whole - awarded) * mult
                        awarded = max(awarded, whole)
                elif bundle and not spread:
                    a['credit'] += judge.place(v, newcomer=newcomer) * mult
                else:
                    a['credit'] += sum(judge.place(p, newcomer=newcomer) for p in pieces) * mult
            elif k == 'padder':
                real = v * 0.4
                a['true'] += real
                a['credit'] += judge.place(real, polished=True, newcomer=newcomer) * mult
            elif k == 'sybil':
                junk = 2.0
                if random.random() < catch:
                    continue  # challenged and removed as fake
                p = judge.place(junk, newcomer=newcomer)
                if p >= cfg.get('threshold', 0):
                    a['credit'] += p * mult
            elif k == 'small':
                tiny = random.uniform(1, 4)
                a['true'] += tiny
                p = judge.place(tiny, newcomer=newcomer)
                if p >= cfg.get('threshold', 0):
                    a['credit'] += p * mult
            else:
                a['true'] += v
                a['credit'] += judge.place(v, newcomer=newcomer) * mult

    total_c = sum(a['credit'] for a in agents)
    total_t = sum(a['true'] for a in agents) or 1
    groups = {}
    for a in agents:
        g = groups.setdefault(a['kind'], [0, 0])
        g[0] += a['credit']
        g[1] += a['true']
    out = {k: (c / total_c, t / total_t) for k, (c, t) in groups.items()}
    out['_gini'] = gini([a['credit'] for a in agents if a['kind'] != 'sybil'])
    return out


def report(name, cfg, runs=40):
    acc = {}
    ginis = []
    for s in range(runs):
        r = run(cfg, s)
        ginis.append(r.pop('_gini'))
        for k, (cs, ts) in r.items():
            acc.setdefault(k, []).append((cs, ts))
    print(f'\n{name}  (gini {statistics.mean(ginis):.2f})')
    for k, rows in acc.items():
        cs = statistics.mean(r[0] for r in rows)
        ts = statistics.mean(r[1] for r in rows)
        ratio = cs / ts if ts else float('inf')
        print(f'  {k:9} credit {cs*100:5.1f}%  value {ts*100:5.1f}%  ratio {ratio if ts else 0:5.2f}')


SPLIT = ('splitter', 2, dict(start=0, rate=0.3, size=25, late=True, k=5))
report('A baseline', {})
report('B splitters, no bundle rule', {'bundle': False, 'extra': [SPLIT]})
report('C splitters, bundle rule', {'bundle': True, 'extra': [SPLIT]})
report('D splitters dodge bundle by spreading across windows', {
    'bundle': True, 'extra': [('splitter', 2, dict(start=0, rate=0.3, size=25, late=True, k=5, across_windows=True))]})
report('E splitters, flatter judge (compression 0.7)', {
    'bundle': False, 'judge': {'compression': 0.7}, 'extra': [SPLIT]})
report('F padders, no length normalisation', {'extra': [('padder', 3, dict(start=0, rate=0.5, size=25, late=True))]})
report('G padders, length normalised', {'judge': {'length_norm': True},
                                        'extra': [('padder', 3, dict(start=0, rate=0.5, size=25, late=True))]})
report('H 20 sybil accounts, 60% caught', {'extra': [('sybil', 20, dict(start=0, rate=1.0, size=0))]})
report('I 20 sybil accounts, 20% caught', {'fraud_catch': 0.2, 'extra': [('sybil', 20, dict(start=0, rate=1.0, size=0))]})
report('J insider judges lowball newcomers 20%', {'judge': {'insider_lowball': 0.2}})

SPREAD = ('splitter', 2, dict(start=0, rate=0.3, size=25, late=True, k=5, across_windows=True))
report('K splitters across windows, cumulative judging per need', {'cumulative': True, 'extra': [SPREAD]})
report('K2 same, flatter judge', {'cumulative': True, 'judge': {'compression': 0.7}, 'extra': [SPREAD]})
SYB = ('sybil', 20, dict(start=0, rate=1.0, size=0))
SMALL = ('small', 5, dict(start=0, rate=0.6, size=0))
report('L junk + honest tiny work, no threshold', {'extra': [SYB, SMALL]})
report('M junk + honest tiny work, below-smallest-reference earns 0 (threshold 5)', {'threshold': 5, 'extra': [SYB, SMALL]})
