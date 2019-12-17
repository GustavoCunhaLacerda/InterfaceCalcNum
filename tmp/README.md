## FUNÇÃO PARA O ELLIAN : ##

A função tem a seguinte assinatura:

```
tratar_func_text(f_text):
	...
	return f_text_final
```


O que ela faz ? A função recebe uma string tipo "2x^2" e transforma retorna "2x\*\*2" substituindo o '^' por '\*\*' já que '^' equivale á uma operação de potência em muitas aplicações.
Outro exemplo: "pow(sen(x), 6)" -> "sin(x)**6"
Algumas das mudanças necessárias são:

Números:
- [ ] "34,123" -> "34.123" (substituir a ',' por '.')

Sintaxe:
- [ ] "[" e "]" -> "(" e ")" respectivamente
- [ ] "{" e "}" -> "(" e ")" respectivamente

- [ ] "A", "a", "B", "b", ..., "Z", "z" -> "x"  ObsImp.: É garantido pelo tratamento de erro que a função só terá uma variável
 
Potência e raízes:
- [ ] "pow(x, y)" ou "pot(x, y)" entre outras variantes -> "x**y"
- [ ] "exp(x)" -> "e**x" -> "2.7182...**x"
- [ ] "x^y" -> "x**y"

- [ ] "sqrt(x)" -> "(x**(1/2))" ou "(x**(0.5))" 
- [ ] "root(y, x)" -> "(x**(1/y))"

Trigonometria:
- [ ] "pi" -> "3.1415..." (bota umas 10/12 casas em pi)
- [ ] "e" -> "2.7182...." (bota umas 10/12 casas em e)
- [ ] "rad(x)" ou "x°" -> transforma x em um valor em radianos


- [ ] "sen(x)" ou "seno(x)" entre outras variantes -> "sin(x)"
- [ ] "cosseno(x)" entre outras variantes -> "cos(x)" 
- [ ] "tg(x)" ou "tangente(x)" entre outras variantes -> "tan(x)" 