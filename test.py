email = ["@fiap", "gustavo@fiap.com.br:senha1", "alan@fiap.com.br:senha2", "alexandre@fiap.com.br:senha3", "aline@fiap.com.br:senha4", "amanda@fiap.com.br:senha5", "bruno@fiap.com.br:senha6", "bruna@fiap.com.br:senha7", "breno@fiap.com.br:senha8", "carla@fiap.com.br:senha9", "carlos@fiap.com.br:senha10", "david@fiap.com.br:senha11", "devid@fiap.com.:senha12", "eduardo@fiap.com.br:senha13", "fabio@fiap.com.br:senha14", "fabiano@fiap.com.br:senha15", "humberto@fiap.com.br:senha16", "iago@fiap.com.br:senha17", "joanatan@fiap.com.br:senha18", "joao@fiap.com.br:senha19", "jonas@fiap.com.br:senha20", "julio@fiap.com.br:senha21", "kleber@fiap.com.br:senha22", "kamila@fiap.com.br:senha23", "marcos@fiap.com.br:senha24", "mauricio@fiap.com.br:senha25", "nicolas@fiap.com.br:senha26", "oscar@fiap.com.br:senha27", "sabrina@fiap.com.br:senha28", "ricardo@fiap.com.br:senha29", "wallace@fiap.com.br:senha30"]
pesquisa = input("Qual o dado deseja vazar= ")

for dado in email:
    if pesquisa == dado:
        print(email)
    else:
        break
