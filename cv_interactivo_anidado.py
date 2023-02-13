pd = 1

def cv_es(pd):
   while pd != 0:
      pd = int(input("Qué te gustaría saber sobre mi? \n\n1) Contame cómo te llamás y algo sobre vos. \n2) Qué herramientas de IT podés ofrecernos? \n3) Actualmente te estás capacitando? Te gustaría capacitarte más? \n4) Si tuvieras que destacar algo sobre vos, qué sería? \n5) Hablás inglés? \n6) Cómo te imaginás a largo plazo? \n7) Llegado al caso, cómo podríamos contactarte?\n0) Cuando ya no tengas más preguntas. \n\nIngresá acá el número de la pregunta deseada: "
))  
      
      if pd == 1:
         print("\nBuenas! Mi nombre es Gabriel, Soy programador autodidacta.\nAmo el estado de mente resolutiva que se desarrolla aprendiendo programación\ny todo lo que tiene que ver con la iteracción con la máquina y los métodos\nque tenemos para acceder a ella.\n")
      elif pd == 2:
         print("\nA lo largo de este tiempo aprendí a usar Python, Java y Javascript\nTuve la oportunidad de entrenar otros lenguajes como Gobstones\ny Ruby en #YoPrgramo de Argentina Programa 4.0\n\nMe interesa mucho la lógica de programación y dado el tiempo\nque le dediqué a aprender, creo tener una base sólida al respecto. \n")
      elif pd == 3:
         print("\nActualmente estoy incorporando herramientas más relacionadas con el trabajo\nen equipo como Git y Github.\nMe siento muy atraído por el Machine Learning y la Inteligencia Artificial\npor lo que siempre ando investigando sobre el tema.\nMe gusta estar siempre desarrollandome y aprendiendo por lo que me encantaría\ntrabajar para una empresa que me pida que crezca en este aspecto.\n")
      elif pd == 4:
         print("\nMe considero una persona ridiculamente optimista de toda la vida\ny creo que justo en este ambiente es algo que me ha ayudado\nmuchísimo a la hora de enfrentarme a problemas que no supe\nen un primer momento cómo resolver.\nCreo que esta característica de mi persona le puede resultar muy productiva\na cualquier empresa con la que trabaje.\n")
      elif pd == 5:
         print("\nYeah, I can speak in english pretty much fluidly.\nAs I can have a standard conversation easily,\nmaybe I'd try harder at my technical english.\n")
         dq = 1
         def cv_en(dq):
            while dq != 5:
                 dq = int(input("\nWhat would you like to know about me? \n\n1) Tell me your name and something about you. \n2) What kind of IT tools could you offer to us? \n3) Talking about IT: Are you getting qualified about something right now? Would you like to train yourself more? \n4) If you had to stand out something about you, what would it be? \n5) Let's go back to the spanish talk \n6) How do you picture yourself in the long terms? \n7) If we'd like to get in touch with you, how we could do it?\n0) When you want to say goodbye. \n\nPut the numer of your desired question here: "
))      
                 if dq == 1 :
                     print("\nHey! My name is Gabriel, I'm selftaught developer.\nI love de decisive state of mind that programming develops in myself\nand everything that is related with the interaction with de machine and the ways\nwe have to deal with it.\n")
                 elif dq == 2:
                     print("\nThrow this time I learned how to use Python, Java y Javascript\nI had the chance to train another languages as Gobstones\nand Ruby at Argentina Programa 4.0's #YoPrgramo\n\nI'Me really interested about logic programming and given the time\nI dedicated to learn it, I believe I have a solid foundation about it. \n")
                 elif dq == 3:
                     print("\nRight now I'm incorporating tools a little more related to the team work\nas Git y Github.\nI feel very attracted to the Machine Learning and IA development\nso I'm always exploring about this issues.\nI like to be always growing up and learning so\nI'd love to work with a corporation that ask for me to do it.\n")
                 elif dq == 4:
                     print("\nI considerate myself a ridiculous optimist since my whole life\nand I believe that in this environment this is something that helped me out a lot\nat the time to deal with problems that I didn't know how to resolve..\n I believe this feature of mine could be result very productive\nto any company that I could work with.\n")
                 elif dq == 6:
                     print("\nI can picture myself developing AI in colaboration with another people.\nI'd love to have a chance to work with another kind of science such\nGiuseppe's de NotCo case, that is an IA that makes similar recipes\n to animal origin products, but 100% plant based.\n")
                 elif dq == 7:
                     print("\nWell, here you have a few ways to get in touch with me:\n\n1159954779\ncoria.gabriel@hotmail.com\nhttps://www.linkedin.com/in/coriagabriel/\nhttps://github.com/funkydluffy\n")
                 elif dq > 7:
                     print("\nThat's not an question I could answer :(\n")
                 elif dq == 0:
                     print("\nThanks for your time!\nGabriel Coria.\n")
                     exit()
         cv_en(dq)
         print ("\nGenial, volvamos al español!\n")
      elif pd == 6:
         print("\nMe imagino desarrollando tecnología con IA en colaboración con otras personas.\nMe gustaría tener la posibilidad de trabajar con otras ciencias como\nen el caso de Giuseppe de NotCo, que es una IA que desarrolla recetas\nsimilares a productos de origen animal, pero 100% a base de plantas.\n")
      elif pd == 7:
         print("\nBueno estas son las formas de contactarme:\n\n1159954779\ncoria.gabriel@hotmail.com\nhttps://www.linkedin.com/in/coriagabriel/\nhttps://github.com/funkydluffy\n")
      elif pd > 7:
         print("\nEsa no es una pregunta que pueda responder en este momento :(\n")

cv_es(pd)
print("\nGracias por tu tiempo!\nGabriel Coria.\n")

exit()