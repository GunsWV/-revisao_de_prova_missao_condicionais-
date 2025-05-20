#Você está sendo avaliado(a) em sua habilidade de tomar decisões automatizadas por meio de códigos. Em cada uma das atividades a seguir, use estruturas condicionais com sabedoria.

#O Sistema de Avaliação da Agência Central de Inteligência precisa classificar os agentes de acordo com sua nota final. Sua missão é automatizar esse processo.

nome_agente = input("Olá, tudo bem? eu sou do sistema de avaliação da agência central de inteligência artificial. Me informe seu nome por gentileza: ")

nota_final = float(input("Agora sua nota final por favor:"))

if 9.0 <= nota_final <= 10.0:
    print(f"Agente {nome_agente}, sua classificação é:Excelente 🏅 (nota: {nota_final})")
elif 7.0 <= nota_final <= 8.9:
    print(f"Agente {nome_agente}, sua classificação é:Bom 👍 (nota: {nota_final})")
elif 5.0 <= nota_final <= 6.9:
        print(f"Agente {nome_agente}, sua classificação é:Regular ⚠️ (nota: {nota_final})")
elif 3.0 <= nota_final <= 4.9:
     print(f"Agente {nome_agente} , sua classificação é:Ruim 🚫 (nota: {nota_final})")
elif 0.0 <= nota_final <= 2.9:
    print(f"Agente {nome_agente}, sua classificação é:Crítico 🚨 (nota: {nota_final})")
else:
    print(f"Agente {nome_agente}, sua classificação é:Nota inválida ❌")