# Derivative of e

e에 대해 공부했다면 $e^x$는 미분해도 $e^x$라는 걸 들어 봤을거다.
이를 증명해보겟다.

$y=e^x &rarr; \frac{\partial y}{\partial x}=e^x$

$\displaystyle{\lim_{h \to 0}} \frac{e^{x+h}-e^x}{h}$

$\displaystyle{\lim_{h \to 0}} \frac{e^x(e^h-1)}{h}$

$e^x\displaystyle{\lim_{h \to 0}} \frac{e^h-1}{h}$

여기서 $e^h-1=t$로 치환하면

$e^x\displaystyle{\lim_{t \to 0}} \frac{t}{\log_et+1}$

$e^x\displaystyle{\lim_{t \to 0}} \frac{\frac{1}{\log_et+1}}{t}$

$e^x\displaystyle{\lim_{t \to 0}} \frac{1}{(\log_et+1) \times \frac{1}{t}}$

$e^x\displaystyle{\lim_{t \to 0}} \frac{1}{\log_e(t+1)^ \frac{1}{t}}$

$e^x\displaystyle{\lim_{t \to 0}} \frac{1}{\log_ee}$

$e^x \times 1 = e^x$
