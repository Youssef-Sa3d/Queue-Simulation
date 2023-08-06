import random


interarrival = []
arrival = []
service = []
begin = []
end = []
wait = []
system = []
idle = []
queue = []


def sum(arr):
    sum  = 0 
    for i in arr:
        sum = sum + i
    return(sum)    

    

def user_input():
    i = int(input("i = "))
    for x in range(i) :
        interarrival.append(int(input( "interarrival = ")))
        service.append(int(input( "service = ")))
        
    arrival.append(interarrival[0])
    begin.append(0)
    end.append(service[0] + begin[0])
    wait.append(abs(arrival[0] - begin[0]))
    system.append(wait[0] + service[0])
    idle.append(0)
    # queue.append(0)
    
        
        
    for x in range( i-1 ):
        arrival.append(arrival[x] + interarrival[x+1])
        
        if end[x] > service[x+1]:
            begin.append(end[x])    
        else:
            begin.append(service[x+1])
        
        end.append(service[x+1] + begin[x+1])
        
        wait.append(abs(arrival[x+1] - begin[x+1]))
        
        system.append(wait[x+1] + service[x+1])
        
        if wait[x] > 0 :
            idle.append(0)
        else:
            idle.append(abs(end[x] - begin[x+1]))
            
                
    for x in range( i ):
        count = 0
        for n in range(x, 0, -1):
            if arrival[x] < begin[n-1]:
                count += 1
            else:
                continue
        queue.append(count)
                
                
                
                
            
    
    
    
    
            

            
        
        
    print("__________________________________________________________")
    print("Interarrival", "  ||  ", "Arrival",
          "  ||  ", "Service", "  ||  ", "Begin", "  ||  ", "End", "  ||  ", "Wait", "  ||  ", "System", "  ||  ", "idle", "  ||  ", "queue")
    print("____________________________________________________________________________________________________________________________________________________________________________")
    for x in range(i):
        print(interarrival[x], "    ||    ",
              arrival[x], "    ||    ", service[x], "    ||    ", begin[x], "    ||    ", end[x], "    ||    ", wait[x], "    ||    ", system[x], "    ||    ", idle[x], "    ||    ", queue[x])
        
        
    avg_wait = sum(wait) / i
    avg_system = sum(system) / i
    avg_servive = sum(service) / i
    avg_interarrival = sum(interarrival) / i
    who_wait = abs( wait.count(0) - len(wait) )
    avg_who_wait = sum(wait) / who_wait
    prob_wait = who_wait / i
    prob_idle = sum(idle) / end[-1]
    server_utilization = 1 - prob_idle
    avg_queue = sum(queue) / i
    
    print("Average wait = " , avg_wait)
    print("Average system  = " , avg_system)
    print("Average service time = " , avg_servive)
    print("Average interarrival = " , avg_interarrival)
    print("Average queue length = " , avg_queue)
    print("Average who wait = " , avg_who_wait)
    print("Probability of wait = " , prob_wait)
    print("Probability of idle = " , prob_idle)
    print("Server utilization = ", server_utilization)


#___________________________________________________________________________________________#

def random_():
    inter = []
    prob1 = []
    cdf1 = []
    ser = []
    prob2 = []
    cdf2 = []
    Ri = []
    
    i = int(input("i = "))
    for x in range(i):
        Ri.append(random.random())
    
    suii = int(input("interarrival prob = "))
    for x in range(suii):
        inter.append(int(input("interarrival = ")))
        prob1.append(float(input("prob = ")))
    cdf1.append(prob1[0])
    for x in range(suii-1):
        cdf1.append(cdf1[x] + prob1[x+1])
    
    print("__________________________________")    
    
    for x in range(suii):
        print(inter[x], " || ", prob1[x], " || ", cdf1[x])
        
    print("__________________________________")
    
    treka = int(input("service prob = "))
    for x in range(treka):
        ser.append(int(input("service = ")))
        prob2.append(float(input("prob = ")))
    cdf2.append(prob2[0])
    for z in range(treka-1):
        cdf2.append(cdf2[z] + prob2[z+1])
        
    print("__________________________________")    
    
    for x in range(treka):
        print(ser[x], " || ", prob2[x], " || ", cdf2[x])
        
    print("__________________________________")
    
    
    for n in range(i):
        for x in range(suii):
            if cdf1[x] >= Ri[n]:
                interarrival.append(inter[cdf1.index(cdf1[x])])
                break
            else:
                continue
        for x in range(treka):
            if cdf2[x] >= Ri[n]:
                service.append(ser[cdf2.index(cdf2[x])])
                break
            else:
                continue
            
    arrival.append(interarrival[0])
    begin.append(0)
    end.append(service[0] + begin[0])
    wait.append(abs(arrival[0] - begin[0]))
    system.append(wait[0] + service[0])
    idle.append(0)

    for x in range(i-1):
        arrival.append(arrival[x] + interarrival[x+1])

        if end[x] > service[x+1]:
            begin.append(end[x])
        else:
            begin.append(service[x+1])

        end.append(service[x+1] + begin[x+1])

        wait.append(abs(arrival[x+1] - begin[x+1]))

        system.append(wait[x+1] + service[x+1])

        if wait[x] > 0:
            idle.append(0)
        else:
            idle.append(abs(end[x] - begin[x+1]))
            
    for x in range(i):
        count = 0
        for n in range(x, 0, -1):
            if arrival[x] < end[n-1]:
                count += 1
            else:
                continue
        queue.append(count)
            
    print("__________________________________________________________")
    print("Interarrival", "  ||  ", "Arrival",
          "  ||  ", "Service", "  ||  ", "Begin", "  ||  ", "End", "  ||  ", "Wait", "  ||  ", "System", "  ||  ", "idle", "  ||  ", "queue")
    print("____________________________________________________________________________________________________________________________________________________________________________")
    for x in range(i):
        print(interarrival[x], "    ||    ",
              arrival[x], "    ||    ", service[x], "    ||    ", begin[x], "    ||    ", end[x], "    ||    ", wait[x], "    ||    ", system[x], "    ||    ", idle[x], "    ||    ", queue[x])
        
    avg_wait = sum(wait) / i
    avg_system = sum(system) / i
    avg_servive = sum(service) / i
    avg_interarrival = sum(interarrival) / i
    who_wait = abs(wait.count(0) - len(wait))
    avg_who_wait = sum(wait) / who_wait
    prob_wait = who_wait / i
    prob_idle = sum(idle) / end[-1]
    server_utilization = 1 - prob_idle
    avg_queue = sum(queue) / i

    print("Average wait = ", avg_wait)
    print("Average system  = ", avg_system)
    print("Average service time = ", avg_servive)
    print("Average interarrival = ", avg_interarrival)
    print("Average queue length = ", avg_queue)
    print("Average who wait = ", avg_who_wait)
    print("Probability of wait = ", prob_wait)
    print("Probability of idle = ", prob_idle)
    print("Server utilization = ", server_utilization)

    
        
# #___________________________________________________________________________________________#

user = int(input("Input (1) or Random (2) ? \n"))
if user == 1 :
    user_input()
elif user == 2 :
    random_()
else:
    print("Error!")
