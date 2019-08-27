def mediaTempo( processo, burstTime): 
  
    tempo = [0] * len(processo)  
    tempoResp = [0] * len(processo)   
    total_tempo = 0
    total_tempoResp = 0
    
    #Buscando tempo de espera de cada proceso
    tempo[0] = 0
  
    #O tempo de espera de um processo sempre vair ser o tempo de espera somado com o burstTime do processo anterior 
    for i in range(1, len(processo)): 
      tempo[i] = burstTime[i - 1] + tempo[i - 1]  

    #Buscando o tempo de resposta de cada processo

    #O tempo de resposta de um processo sempre vai ser o seu tempo de espera + burstTime
    for i in range(len(processo)): 
      tempoResp[i] = burstTime[i] + tempo[i]
     
    print ('*-------------------------------------------------------*')
    print( "| Processo | Burst time | Tempo Espera | Tempo Resposta |") 
    print ('*-------------------------------------------------------*')
  
    for i in range(len(processo) ): 
        total_tempo += tempo[i] 
        total_tempoResp += tempoResp[i] 
        print(" " + str(processo[i]) + "\t\t" + str(burstTime[i]) + "\t\t\t " + str(tempo[i]) + "\t\t\t\t " + str(tempoResp[i]))  

    print ('*-------------------------------------------------------*')
    print( "Média tempo de espera = " + str(total_tempo / len(processo) )) 
    print("Média tempo de resposta = " + str(total_tempoResp / len(processo))) 
  
if __name__ == "__main__": 

    processo = [ 'word   ', 'chrome  ', 'sublime'] 

    burstTime = [10, 15, 8] 
  
    mediaTempo(processo, burstTime) 