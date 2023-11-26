contatos = {
    "Clark Kent":
    {"celular": "123456",
    "Email":"Super@Krypton.com"},
"Bruce Wayne":

{"celular":"654321",
 
 "Email":"bat@caverna.com.br"}

}
#esse for passará por todos os items do dicionário contatos, com a variável "contato" contendo as chaves desses items e o objeto formas contendo os valores, que são os dicionários de formas de contatos
for contato, formas in contatos.items():
    #para cada item encontrado no dicionário anterior, que estão contidos no dicionário "formas", vamos recuerar as chaves "celular" e "email" e seus valores
    for celular, email in formas.items():
        #exibimos aqui o nome do contato e as suas formas de contato
        print("O contato {} pode ser encontrado no celular {} e no email {}".format(contato, celular, email))



