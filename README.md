# Fertilizacao

  A fertilização é um processo complexo na agricultura. Saber quanto e quais fertilizantes aplicar é muito importante. Aplicar a menos resulta num sub rendimento da cultura, aplicar a mais significa uma perda económica acentuada e possíveis problemas ambientais. Com os manuais e as técnicas de fertilização a serem alterados periodicamente, um programa ajuda imenso os agricultores a conseguirem tomar a decisão mais acertada possível.
O nosso projeto tem como objetivo auxiliar a fertilização com base em resultados de análises de solo. Para tal iremos precisar de 3 principais inputs dados pelo utilizador


# Análises de solo

  Saber a quantidade de nutrientes já presentes no solo é essencial para uma fertilização correta. Estes dados têm de ser dado pelo utilizador, que por sua vez os vai buscar a um laboratório. Os inputs que o programa pede, são os mesmos que aparecem descritos nas análises de solo em Portugal. Pelas análises atribuimos classes de fertilidade para alguns nutrientes (Potássio, Magnésio e Fósforo). O azoto é o mais complexo, nao tendo relação direta, iremos ter de criar várias funções. O azoto presente no solo é calculado atraves da percentagem de MO e da cultura anterior.


# Culturas
  Decidimos fazer a recomendação para quatro culturas diferentes: (ervilha, melancia, beterraba e beringela). Para isto definimos classes, em que cada classe apresentava as necessidades de fertilização de cada cultura, para os diferentes niveis de classes de fertilidade. Aqui foi onde tivemos mais dificuldade pois as tabelas com duas entradas foram trabalhosas de passar para classes.
