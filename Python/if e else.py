#Else sempre vai referenciar um IF na indentação
if tempo == bom:
    if ir_ao_restaurante():
        almoçar()
    else:
        comer_hotdog()
else:
    if ir_ao_teatro:
        comprar_ingresso()
    else:
        ir_ao_shopping()

#elif = verifica mais do que uma condição e para quando a 1º for verdadeira
#if-elif-else

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()
