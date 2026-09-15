# Research plan: approximating Rényi divergences beyond independent coordinates

Date: 16 September 2026  
Status: research programme with elementary derivations and a tested obstruction; no general dependent law approximation theorem is claimed.

## 1. The question to solve

The intended analogue of the motivating paper is an algorithm which approximates a divergence on a long observation sequence without enumerating every sequence, with a rigorous probability of success and explicit computational cost.

An important correction determines the scope. For independent coordinates,

$$
P=\bigotimes_{i=1}^n P_i,\qquad Q=\bigotimes_{i=1}^n Q_i,
$$

Rényi divergence satisfies

$$
D_\alpha(P\Vert Q)=\sum_{i=1}^n D_\alpha(P_i\Vert Q_i).
$$

Identical distribution is unnecessary. This is an established property, not a research conjecture [R2, Theorem 28]. Explicit finite marginals already give a direct computation with work proportional to their total size, under an arithmetic model which counts the required elementary functions at unit cost.

Accordingly, interpret the substantive question as follows:

> Can predictable increment methods give rigorous and computationally useful approximation guarantees for Rényi divergence between dependent sequence laws with tractable conditional probabilities?

The first concrete targets are finite mixtures of products and the observed laws of small hidden Markov models. Products conditioned on a common selection event form a separate, particularly useful route. These are modelling choices for this programme, not assumptions about what the user originally intended.

A composite optimisation is another distinct problem. Even when each fixed pair of laws is a product, a parameter shared across coordinates can prevent an infimum or supremum from separating. Pairwise additivity still holds. Do not confuse failure of that optimisation to separate with failure of divergence additivity, or replace a composite family by a mixture without specifying why that is the desired target.

## 2. What to borrow from the paper

Anand, Benford and Guo [R1] obtain relative approximation of total variation between explicit product laws in time proportional to $nq\varepsilon^{-2}\log(1/\delta)$. Their estimator sums predictable changes in a posterior quantity. Its second moment argument bounds the expected remaining gain using product structure. The transferable idea is the predictable sum; the independence dependent bound must be replaced, not assumed.

Filtered Monte Carlo itself predates this paper [R3]. A new posterior identity alone would not establish novelty. The research contribution must concern assumptions, error guarantees, cost, or a sharp obstruction for a specific model class.

## 3. Targets, access model and conventions

Use natural logarithms. For finite laws define the power integral and its nonnegative gap by

$$
H_\alpha(P,Q)=\sum_x P(x)^\alpha Q(x)^{1-\alpha},
\qquad
\Delta_\alpha(P,Q)=\operatorname{sgn}(\alpha-1)\bigl(H_\alpha(P,Q)-1\bigr).
$$

Then

$$
D_\alpha(P\Vert Q)=\frac{\log H_\alpha(P,Q)}{\alpha-1}.
$$

For $0<\alpha<1$, $\Delta_\alpha=1-H_\alpha$. For $\alpha>1$, $\Delta_\alpha=H_\alpha-1$. Distinguish all three quantities in code, plots and theorem statements.

The primary order range is a fixed compact subset of $(0,1)$, beginning with $\alpha=1/2$. Treat orders above one as a separate work package. Orders zero, one and infinity require separate support or limiting arguments and are not included in the initial theorem target.

Write arbitrary sequence laws as

$$
P(x_{1:n})=\prod_{i=1}^n p_i(x_i\mid x_{<i}),
\qquad
Q(x_{1:n})=\prod_{i=1}^n q_i(x_i\mid x_{<i}).
$$

These are products of conditional probabilities, not product measures. Initially assume a finite alphabet and strictly positive probabilities, then extend support semantics explicitly.

The basic access model supplies both full conditional probability vectors at a visited history and permits exact sequential sampling. Let $C_{\rm path}$ include all filtering, probability evaluation, elementary function evaluation and sampling costs for one trajectory. An algorithm requiring conditional probabilities is not automatically efficient when only joint likelihood evaluation or unconditional sampling is available. Computing those conditionals may itself be the hard inference problem.

The principal guarantee should ultimately be

$$
\Pr\{(1-\varepsilon)D_\alpha\leq\widehat D_\alpha\leq(1+\varepsilon)D_\alpha\}\geq1-\delta.
$$

Intermediate theorems may concern relative error in $\Delta_\alpha$ or additive error in $D_\alpha$, but must be named accordingly. At zero divergence, multiplicative accuracy requires exact zero on the success event. Do not assume that equality of two hidden observation models can be recognised by comparing their parameter arrays.

## 4. Exact controls before approximation

**Independent, nonidentical coordinates.** Implement the exact additive formula as the first control. It removes any possibility of presenting a Monte Carlo approximation as necessary for this setting.

**Observed Markov chains.** Suppose the initial laws are $\mu_P,\mu_Q$ and the transition matrices are $K_i^P,K_i^Q$, possibly varying with time. Define

$$
v_1(x)=\mu_P(x)^\alpha\mu_Q(x)^{1-\alpha},
\qquad
T_i(x,y)=K_i^P(x,y)^\alpha K_i^Q(x,y)^{1-\alpha}.
$$

Then ordinary summation over paths gives

$$
H_\alpha=v_1^{\mathsf T}T_2\cdots T_n\mathbf1.
$$

For dense $q$ state matrices this costs $O(nq^2)$ arithmetic operations. This is an elementary dynamic programming baseline, not the intended novelty. Include the initial factor and all finite horizon boundary terms. A spectral divergence rate is not a replacement for this finite horizon quantity.

**Hidden states.** The previous formula does not compute the divergence of the observations after hidden paths have been summed out. Taking a noninteger power of a sum does not commute with summation. The divergence of an augmented hidden and observed law is a different target.

**Tiny models.** Enumerate all observation paths to calculate exact algebraic means and second moments of candidate estimators, evaluated at increased numerical precision where necessary. Enumeration is a validation tool, not an efficient algorithm.

## 5. A predictable estimator which survives dependence

The following is an elementary derivation made for this plan. It is not asserted to be a new identity in the literature.

Draw a single fair hypothesis label $J\in\{P,Q\}$ and generate an entire path from that law. Let $M=(P+Q)/2$ and let $\mathcal F_i$ contain only the observations through time $i$, not the hidden simulation label. Set

$$
a_i=\Pr(J=P\mid\mathcal F_i),\qquad b_i=1-a_i,
\qquad a_0=b_0=1/2.
$$

At a visited history $h=x_{<i}$, define

$$
z_i(h)=\sum_c p_i(c\mid h)^\alpha q_i(c\mid h)^{1-\alpha},
\qquad
w_\alpha(a)=2a^\alpha(1-a)^{1-\alpha}.
$$

Compute the increment before sampling the next symbol:

$$
C_i=\operatorname{sgn}(\alpha-1)\,
       w_\alpha(a_{i-1})\bigl(z_i(h)-1\bigr),
\qquad A_\alpha=\sum_{i=1}^n C_i.
$$

Update the posterior using both conditional laws:

$$
a_i=\frac{a_{i-1}p_i(X_i\mid h)}
 {a_{i-1}p_i(X_i\mid h)+b_{i-1}q_i(X_i\mid h)}.
$$

For strictly positive finite laws, every increment is nonnegative and

$$
\boxed{\mathbb E_M A_\alpha=\Delta_\alpha(P,Q).}
$$

### Proof

Let $s=\operatorname{sgn}(\alpha-1)$ and introduce

$$
\Phi_\alpha(a)=2s\left[a^\alpha(1-a)^{1-\alpha}
 -\alpha a-(1-\alpha)(1-a)\right].
$$

This function is convex and vanishes at $a=1/2$. Since $a_i$ is a posterior martingale, its affine terms have zero conditional drift. Bayes' rule gives

$$
\mathbb E_M[w_\alpha(a_i)\mid\mathcal F_{i-1}]
   =w_\alpha(a_{i-1})z_i(h).
$$

Therefore $C_i$ is the conditional drift of $\Phi_\alpha(a_i)$ and is nonnegative. At the final time,

$$
\mathbb E_M w_\alpha(a_n)=H_\alpha(P,Q),
\qquad
\mathbb E_M a_n=1/2.
$$

Taking expectations and telescoping proves the identity.

### Algorithmic status

The result supplies an unbiased estimator of the gap, not of the logarithmic divergence. Taking a logarithm of a sample mean is generally biased. One trajectory costs $C_{\rm path}$, but its variance determines how many trajectories are necessary.

For $0<\alpha<1$,

$$
0\leq w_\alpha(a)\leq B_\alpha
 :=2\alpha^\alpha(1-\alpha)^{1-\alpha}\leq2.
$$

For $\alpha>1$ this weight is unbounded as the posterior probability of $Q$ approaches zero. This is one reason to keep the two order ranges separate.

## 6. The actual theorem target: control the remaining gain

For a history before step $i$, let $P_i^h,Q_i^h$ denote the conditional laws of the entire remaining observation sequence. Conditional telescoping yields

$$
R_i(h):=\mathbb E_M\!\left[\sum_{j=i}^n C_j\mid\mathcal F_{i-1}\right]
 =w_\alpha(a_{i-1})\Delta_\alpha(P_i^h,Q_i^h).
$$

This formula identifies exactly what must replace independence.

### Conditional second moment lemma

Suppose a known constant $K\geq1$ satisfies

$$
R_i(h)\leq K\Delta_\alpha(P,Q)
$$

at every history of positive mixture probability. Then

$$
\mathbb E_M A_\alpha^2\leq2K\Delta_\alpha(P,Q)^2.
$$

Indeed,

$$
A_\alpha^2=2\sum_i C_i\sum_{j=i}^nC_j-\sum_i C_i^2.
$$

Because $C_i$ is measurable before step $i$, taking expectations gives

$$
\mathbb E A_\alpha^2
 =2\sum_i\mathbb E[C_iR_i]-\sum_i\mathbb E C_i^2
 \leq2K\Delta_\alpha\mathbb E A_\alpha.
$$

This proves the assertion. The lemma is elementary; deriving a useful $K$ from model parameters is the research problem. A definition of $K$ involving unknown conditional divergences is not a computable algorithmic guarantee.

For $\Delta_\alpha>0$, the relative variance is at most $2K-1$. Means of independent repetitions followed by a median give relative gap error $\eta$ with failure probability $\delta$ using

$$
O\!\left(K\eta^{-2}\log(1/\delta)\right)
$$

trajectories. For example, use groups of at least $\lceil8K/\eta^2\rceil$ trajectories and an odd number of groups at least $8\log(1/\delta)$. Independence of repetitions is required.

In the product control case with $0<\alpha<1$, each suffix gap is at most the full gap, so $K=B_\alpha$ suffices. This checks the mechanism but adds no computational benefit over exact additivity.

### A rare history counterexample

Let the first observation $B$ have the same Bernoulli$(\tau)$ law under $P$ and $Q$. Given $B=0$, the second observation has the same fair binary law under both. Given $B=1$, its laws are

$$
R=(3/4,1/4),\qquad S=(1/4,3/4).
$$

Put $d_\alpha=\Delta_\alpha(R,S)>0$. The first increment vanishes, the posterior before the second observation is still $1/2$, and

$$
A_\alpha=d_\alpha\mathbf1_{\{B=1\}},\qquad
\Delta_\alpha(P,Q)=\tau d_\alpha.
$$

Consequently,

$$
\frac{\mathbb E A_\alpha^2}{(\mathbb E A_\alpha)^2}=\frac1\tau,
\qquad
\frac{\operatorname{Var}(A_\alpha)}{(\mathbb E A_\alpha)^2}=\frac1\tau-1.
$$

The relative variance is arbitrarily large already at horizon two. Every path has positive probability, and the full likelihood ratio stays between $1/3$ and $3$. Thus positivity, a short horizon, and a bounded likelihood ratio do not by themselves provide a uniform relative gap variance bound for this estimator.

This is not an impossibility theorem for all algorithms. The example is an observed Markov model and is exactly computable. Explicitly summing over the gate also removes its simulation variance. Preserve this distinction in every report.

## 7. Three concrete research routes

### Route A: finite mixtures of product laws

Start with

$$
P(x)=\sum_{r=1}^{m_P}u_r\prod_i p_{ri}(x_i),
\qquad
Q(x)=\sum_{s=1}^{m_Q}v_s\prod_i q_{si}(x_i).
$$

Their observed laws need not be products, but component posterior weights give the required conditional vectors. For explicit finite marginals, a trajectory can be processed in $O(nq(m_P+m_Q))$ arithmetic work.

Compare the direct predictable estimator with stratification over the simulated mixture component. In the latter, estimate the same observable path functional conditionally on each component and average using the known weights. Do not change the target to the divergence between augmented component and observation laws.

The immediate question is whether component integration or block conditioning prevents a small mixing weight from creating the rare gate failure. Seek bounds with explicit dependence on component count, weights and observable separation. Do not assume that positive weights alone settle the problem; cancellation between components can make observed laws very close.

### Route B: hidden Markov observation laws

Use two or three hidden states and a binary observation alphabet initially. Maintain the two model filters along the same observed path. For standard dense finite state models, conditional vector evaluation has per step cost $O(k_P^2+k_Q^2+q(k_P+k_Q))$.

Investigate whether quantitative forgetting of the filters, together with explicit control of informative rare histories, bounds $R_i/\Delta_\alpha$. The required theorem must state the initial distribution, transition and emission assumptions and show every parameter in $K$.

Do not infer this bound merely from mixing of the latent chain. In particular, an additive filter approximation error can overwhelm a very small divergence. If a uniform $K$ fails, investigate block integration, stratification, or a weaker additive divergence guarantee.

Existing work analyses Rényi divergence rates for hidden Markov models and provides specialised numerical methods [R4]. Audit that work before claiming novelty for a finite horizon algorithm. The target here is a finite horizon accuracy and cost guarantee, not just existence of a limiting rate.

### Route C: products conditioned on selection

Let $P_0,Q_0$ be product laws and $E$ a common event with positive probability under both. Define the tilted product law

$$
T_\alpha(x)=\frac{P_0(x)^\alpha Q_0(x)^{1-\alpha}}
 {H_\alpha(P_0,Q_0)}.
$$

Direct substitution gives the exact reduction

$$
H_\alpha(P_0(\cdot\mid E),Q_0(\cdot\mid E))
 =H_\alpha(P_0,Q_0)
 \frac{T_\alpha(E)}{P_0(E)^\alpha Q_0(E)^{1-\alpha}}.
$$

Equivalently, the conditioned divergence is the base divergence plus

$$
\frac{\log T_\alpha(E)-\alpha\log P_0(E)
 -(1-\alpha)\log Q_0(E)}{\alpha-1}.
$$

This converts one dependent law problem into three event probability calculations under product laws. For events defined by a small automaton or an additive statistic, first investigate exact dynamic programming and controlled discretisation. For general rare events, count the event probability estimation cost explicitly.

Cancellation in the displayed logarithmic expression can make relative divergence accuracy harder than relative accuracy of its three inputs. Different conditioning events also require a separate support analysis; the displayed formula concerns a common event only.

## 8. Orders above one and a second estimator family

The predictable identity still holds for strictly positive finite laws, but high likelihood ratio moments can dominate. A local likelihood ratio bound can accumulate exponentially along a path. It must not be treated as a bound independent of the horizon.

A useful alternative starts with

$$
r_i(c\mid h)=\frac{p_i(c\mid h)^\alpha q_i(c\mid h)^{1-\alpha}}{z_i(h)}.
$$

When each normaliser is positive and finite, sampling a path under these local tilted kernels gives the exact importance sampling identity

$$
H_\alpha(P,Q)=\mathbb E_r\prod_{i=1}^n z_i(X_{<i}).
$$

For products, the normalisers are deterministic. For dependent laws they are random, and their product can have large variance. This motivates sequential Monte Carlo and improved proposal kernels, not a free approximation theorem.

The ideal proposal would use the backward continuation function

$$
F(h)=\sum_c p(c\mid h)^\alpha q(c\mid h)^{1-\alpha}F(hc),
\qquad F(x_{1:n})=1,
$$

with transition proportional to $p^\alpha q^{1-\alpha}F(hc)$. Computing $F$ exactly already solves the original summation. Any approximate use must include both its construction cost and its accumulated error.

Review finite sample particle normalising constant results [R5]. A bound with relative variance proportional to $n/N$ requires particle count growing with $n$ for fixed relative accuracy and therefore can lead to quadratic total work. Report the actual dependence on $n,N,\alpha$ and model parameters, rather than describing every sequential method as linear time.

## 9. Converting a gap or power estimate into a divergence estimate

This conversion is part of the theorem, not a numerical afterthought.

For $0<\alpha<1$,

$$
D_\alpha=\frac{-\log(1-\Delta_\alpha)}{1-\alpha}.
$$

If $|\widehat\Delta-\Delta|\leq\eta\Delta$ and $\eta\Delta<H=1-\Delta$, the mean value theorem gives

$$
\frac{|\widehat D-D|}{D}
\leq\frac{\eta\Delta}{(H-\eta\Delta)(-\log H)}.
$$

Thus a relative gap approximation transfers well near equality but not uniformly when $H$ is very small. For a promised $\Delta\leq\gamma<1$, choosing $\eta=\varepsilon(1-\gamma)/2$, with $0<\varepsilon\leq1$, is sufficient. Without such a promise, use a separate power integral estimate or report an interval which may have an infinite upper endpoint.

For $\alpha>1$, concavity of $\log(1+x)$ shows that a relative $\eta$ approximation of the nonnegative gap transfers to a relative $\eta$ approximation of the divergence, for $0<\eta<1$. The difficulty in this range is obtaining the gap guarantee in the first place.

A multiplicative power integral estimate with relative error $\eta<1$ gives additive divergence error at most

$$
\frac{-\log(1-\eta)}{|\alpha-1|}.
$$

It does not automatically give relative divergence accuracy near $D_\alpha=0$.

Support conventions must remain exact. For $0<\alpha<1$, a zero overlap integral means infinite divergence. For $\alpha>1$, positive $P$ mass outside the support of $Q$ means infinite divergence. Sampling cannot rule out an unseen support violation without a structural support check or an explicit promise.

## 10. Numerical and experimental discipline

Store logarithms of prefix likelihoods and use stable posterior calculations. Use `log1p` and `expm1` for small gaps and compare against increased precision references. Merely moving calculations into logarithms does not prevent cancellation near equality. Never add small positive masses to repair support, or clip an invalid estimate into a valid range and call it an accuracy guarantee.

The initial standard library reference code is deliberately restricted to small models. Its Markov and predictable routines require strictly positive input; the separate finite alphabet power integral handles exact zeros. It uses ordinary floating point and is not a stable production implementation for extreme orders, long paths or extremely small gaps.

The initial deterministic suite checks product additivity, Markov recursion, predictable unbiasedness, the rare gate second moment, support conventions, the conditioned product identity and the order above one error conversion. These are regression checks, not proofs of the research targets.

Prespecify the following experiment families:

| Family | What it tests |
| --- | --- |
| Equal and nearby nonidentical products | Zero behaviour, cancellation and the exact control |
| Positive observed Markov models | Agreement with the finite horizon matrix recursion |
| Common rare gate, varying $\tau$ | The predicted $1/\tau$ second moment ratio |
| Small product mixtures | Component cancellation and the effect of stratification |
| Small hidden Markov observation models | Filtering costs and history dependent variance |
| Common selection events | The tilted event reduction and rare event cost |
| Decreasing overlap and orders above one | Logarithmic conversion and tail sensitivity |

Record exact model specifications, order, horizon, seed when randomness is used, path or particle count, method, runtime, estimated variance, error against the exact value when available, and interval coverage. Separate statistical, numerical and model approximation errors. Include favourable and deliberately adverse examples.

## 11. Work packages and completion conditions

| Stage | Work | Required output before advancing |
| --- | --- | --- |
| 0 | Audit definitions and related work | A scope note and a novelty comparison, including rates versus finite horizons |
| 1 | Independently verify the elementary identities | Reviewed derivations and deterministic regression tests |
| 2 | Analyse the unmodified predictable estimator | The rare gate failure retained as a permanent regression example |
| 3 | Build exact mixture and hidden observation oracles | Enumeration agreement and measured oracle costs |
| 4 | Develop a model specific variance result | A proved bound from explicit model parameters, or a precise failure result |
| 5 | Modify sampling where necessary | A stratified, block or tilted estimator with an explicit bias and variance analysis |
| 6 | Prove the requested error conversion | A finite horizon divergence guarantee with all promises stated |
| 7 | Run the prespecified comparison | Reproducible accuracy, coverage and cost results |
| 8 | Decide the paper claim | A narrow theorem supported by proofs and experiments, not by favourable plots alone |

Stages 1 and 2 have initial derivations and small deterministic checks in this workspace. They still need independent mathematical review. Stages 3 onward are research tasks, not completed results.

A successful first theorem would identify a genuinely dependent observation class for which relative gap error $\eta$ is achievable in

$$
O\!\left(C_{\rm path}K\eta^{-2}\log(1/\delta)\right)
$$

work, with a useful explicit $K$, followed by a justified divergence conversion. Linear dependence on the horizon can only be claimed when both the path cost and the required number of paths permit it.

An equally informative outcome is a precise obstruction for a natural estimator together with a demonstrably better alternative, or a useful finite horizon additive divergence guarantee. Do not promote the conditional second moment lemma alone into a model specific approximation theorem.

## 12. Immediate next task

Read `prompts/01_foundations.md`. Independently check Sections 5, 6 and 9, reproduce the twelve deterministic tests, and implement a two component product mixture oracle. Compute exact predictable first and second moments on short paths before running large simulations. Compare direct sampling with integration over the mixture component. The first unresolved question is whether this removes the rare component obstruction without silently estimating a different divergence.

## References and reading status

**[R1]** Konrad Anand, Alistair Benford and Heng Guo. *Linear time approximation of the TV distance between product distributions*. arXiv:2607.27088v1, 2026. HTML read; the author hosted PDF was also inspected, including the second moment proof. [HTML](https://arxiv.org/html/2607.27088) · [Author PDF](https://homepages.inf.ed.ac.uk/hguo/papers/linear-dtv.pdf).

**[R2]** Tim van Erven and Peter Harremoës. *Rényi Divergence and Kullback–Leibler Divergence*. IEEE Transactions on Information Theory, 2014. Theorem 28 checked for nonidentical product additivity. [Text](https://arxiv.org/html/1206.2459v2).

**[R3]** Paul Glasserman. *Filtered Monte Carlo*. Mathematics of Operations Research 18, 610–634, 1993. Bibliographic record and abstract checked; a full comparison of the variance hypotheses remains part of Stage 0. [Author institution record](https://business.columbia.edu/faculty/research/filtered-monte-carlo).

**[R4]** Cheng-Der Fuh, Su-Chi Fuh, Yuan-Chen Liu and Chuan-Ju Wang. *Rényi Divergence in General Hidden Markov Models*. arXiv:2106.01645v1, 2021. Theorem III.1 and the computational section checked to distinguish divergence rates from the present target. Check the final published version during Stage 0. [Text](https://arxiv.org/html/2106.01645v1).

**[R5]** Frédéric Cérou, Pierre Del Moral and Arnaud Guyader. *A nonasymptotic theorem for unnormalized Feynman–Kac particle models*. Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 47, 629–649, 2011. Record and abstract checked; theorem assumptions must be audited before applying a particle variance bound. [Journal record](https://www.numdam.org/articles/10.1214/10-AIHP358/).

Also investigate the older literature on Hellinger processes and predictable divergence processes before assigning novelty to Section 5. This is a literature task, not a claim that the bibliography is exhaustive.
