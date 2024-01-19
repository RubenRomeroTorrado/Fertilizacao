# Fertilizacao

  A fertilização é um processo complexo na agricultura. Saber quanto e quais fertilizantes aplicar é muito importante. Aplicar a menos resulta num sub rendimento da cultura, aplicar a mais significa uma perda económica acentuada e possíveis problemas ambientais. Com os manuais e as técnicas de fertilização a serem alterados periodicamente, um programa ajuda imenso os agricultores a conseguirem tomar a decisão mais acertada possível.
O nosso projeto tem como objetivo auxiliar a fertilização com base em resultados de análises de solo. Para tal iremos precisar de 3 principais inputs dados pelo utilizador


# Análises de solo

  Saber a quantidade de nutrientes já presentes no solo é essencial para uma fertilização correta. Estes dados têm de ser dado pelo utilizador, que por sua vez os vai buscar a um laboratório. Os inputs que o programa pede, são os mesmos que aparecem descritos nas análises de solo em Portugal. Pelas análises atribuimos classes de fertilidade para alguns nutrientes (Potássio, Magnésio e Fósforo). O azoto é o mais complexo, nao tendo relação direta, iremos ter de criar várias funções. O azoto presente no solo é calculado atraves da percentagem de MO e da cultura anterior.


# Culturas
  Decidimos fazer a recomendação para quatro culturas diferentes: (ervilha, melancia, beterraba e beringela). Para isto definimos classes, em que cada classe apresentava as necessidades de fertilização de cada cultura, para os diferentes niveis de classes de fertilidade. Aqui foi onde tivemos mais dificuldade pois as tabelas com duas entradas foram trabalhosas de passar para classes. Fomos buscar os dados ao manual de fertilizantes, lançado pelo INIAV.

# Fertilizantes 
  Criamos uma classe com todos os fertilizantes que poderemos recomendar, e através das análises de solo, produção esperada, cultura e chuva o nosso programa irá fornecer a quantidade de cada fertilizante a aplicar.As formulas de fertilizantes foi-nos dada na cadeira Fertilizantes e Técnicas de Fertilização.

# Ficheiros a enviar
pytest_potassio - Este ficheiro testa a função que atribui a classe de  fertilidade pelo fosforo extraível do solo

pytest_magnesio - Este ficheiro testa a função que atribui a classe de  fertilidade pelo magnésio extraível do solo

pyteste_cultura_anterior - Este ficheiro testa a função que calcula a quantidade de azoto a deduzir das recomendações com base na cultura anteriormente instalada


# O nosso programa

O programa começa por exibir correr uma função que analise as condições precentes no solo, atribuindo classes de fertilidade e azoto deduzivel da fertelização.

Em seguida é corrida uma classe que nos mostra as necessidades de fertilização com base nos dados dados em cima, dizendo tambem se o ph é adequado ou não a cultura

Após isso o utilizador pode selecionar que cultura pretende, e é tambem perguntado se a cultura já se encontra instalada ou nao, e se irá chover nos dias seguintes

Com esta informaçao e com uma classe contendo os fertilizantes disponiveis no mercado, é calcuada a quantidade de cada um a aplicar á cultura.













