# Função para encontrar o tempo de todos os processos 
def tempoEsperaProcesso(processo, n, burst_time, tempo): 
    tempo[0] = 0
   
    for i in range(1, n ): 
        tempo[i] = burst_time[i - 1] + tempo[i - 1]  
  
def tempoRespostaProcesso(processo, n, burst_time, tempo, tempoResp): 

    for i in range(n): 
        tempoResp[i] = burst_time[i] + tempo[i] 

def mediaTempo( processo, n, burst_time): 
  
    tempo = [0] * n 
    tempoResp = [0] * n  
    total_tempo = 0
    total_tempoResp = 0
  
    tempoEsperaProcesso(processo, n, burst_time, tempo) 
  
    tempoRespostaProcesso(processo, n, burst_time, tempo, tempoResp) 
  
    print( "processo Burst time " + " Waiting time " + " Turn around time") 
  
    for i in range(n): 
      
        total_tempo = total_tempo + tempo[i] 
        total_tempoResp = total_tempoResp + tempoResp[i] 
        print(" " + str(i + 1) + "\t\t" + str(burst_time[i]) + "\t " + str([i]) + "\t\t " + str(tempoResp[i]))  
  
    print( "Média tempo de espera = " + str(total_tempo / n)) 
    print("Média tempo de resposta = " + str(total_tempoResp / n)) 
  
if __name__ == "__main__": 
      
    processo = [ 1, 2, 3] 
    n = len(processo) 
  
    burst_time = [10, 5, 8] 
  
    mediaTempo(processo, n, burst_time) 