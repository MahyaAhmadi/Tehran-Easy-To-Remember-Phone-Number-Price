import numpy as np
from itertools import combinations
import pickle
 
# 1-8-7-8-6-2-6
# 1(1)8(2)7(3)8(4)6(5)2(6)6
all_comb = []
for nc in range(1, 7):
   comb = list(combinations([1,2,3,4,5,6], nc))
   for it in range(len(comb)):    
       all_comb.append(comb[it])

#len(all_comb)
#all_comb


def all_how2read(phone_num, all_comb):

#phone_num = '09121878626'

    phext = [*phone_num[4:]]

    allhow2read = []
    for i in range(len(all_comb)):
      
       h2r = []   
       h2r.append(''.join(phext[ : all_comb[i][0]]))
       [h2r.append(''.join(phext[all_comb[i][k]: all_comb[i][k+1]])) for k in range(len(all_comb[i])-1)] 
       h2r.append(''.join(phext[all_comb[i][-1] : ]))
   
       allhow2read.append(h2r)
   
#how2read = np.array(how2read, dtype=object)

#phext, allhow2read

    return phext, allhow2read


all_how2read_ = lambda _: all_how2read(_, all_comb)


def RoundFeatures(phonNumber):       
    phext, allhow2read = all_how2read_(phonNumber)
    #phext, allhow2read

    #len(set(phext))
    #unique_ = list(set(h[3:]))
    #unique, counts = np.unique(phext, return_counts=True)
    #uc_dic= dict(zip(unique, counts))

    # tedade_adad
    #unique, counts, unique.size #len(unique_) #unique.size


    feature_name = {}
    feature_vector = np.zeros((139,))
   
    RaghamAval = [f'RaghamAval{i}' for i in range(10)]
    RaghamDovom = [f'RaghamDovom{i}' for i in range(10)]

    roundType = np.array(['Ayeneie_21', 'Ayeneie_22', 'Ayeneie_23', 'Ayeneie_31', 'Ayeneie_32', 'Ayeneie_33',\
            'Tarazuie',\
                'Pleie21', 'Pleie22' ,'Pleie31' ,'Pleie23', 'Pleie32', 'Pleie24', 'Pleie25','Pleie33' ,'Pleie34',\
                    'Joft21', 'Joft22', 'Joft23', 'Joft26', 'Joft24', 'Joft25', 'Joft31', 'Joft32',\
                        'DahDahi11', 'DahDahi12' ,'DahDahi21', 'DahDahi22', 'DahDahi31', 'DahDahi32', 'DahDahi41' ,'DahDahi42', 'DahDahi13', 'DahDahi14', 'DahDahi23', 'DahDahi24',\
                            'SadSadi11' ,'SadSadi12' ,'SadSadi21', 'SadSadi22',\
                                'CodeHezari11', 'CodeHezari12', 'CodeHezari13', 'CodeHezari21', 'CodeHezari22', 'CodeHezari23', 'CodeHezari14', 'CodeHezari24', \
                                    'CodeDahHezari11', 'CodeDahHezari12', 'CodeDahHezari21', 'CodeDahHezari22',\
                                        'CodeMiluni',\
                                            'َAz2adad',\
                                                '3raghamAvalYeki','4raghamAvalYeki', '5raghamAvalYeki', '6raghamAvalYeki',\
                                                    '3raghamAkharYeki', '4raghamAkharYeki', '5raghamAkharYeki', '6raghamAkharYeki',\
                                                        '7raghamYeki',\
                                                            '3raghamVasatYeki01', '3raghamVasatYeki02', '3raghamVasatYeki03','4raghamVasatYeki01','4raghamVasatYeki02','5raghamVasatYeki', \
                                                                'CodePaien1', 'CodePaien2', 'CodePaien3', 'CodePaien4', 'CodePaien5',\
                                                                    'TarikhTavalodS1', 'TarikhTavalodS2', 'TarikhTavalodM1', 'TarikhTavalodM2', \
                                                                        'PishShomreA01', 'PishShomreA02', 'PishShomreB01', 'PishShomreB02', \
                                                                            'CodeRiz','doRaghamYeki24','doRaghamYeki23','doRaghamYeki22','doRaghamYeki21','doRaghamYeki25','doRaghamYeki26',\
                                                                                'TartibiA02', 'TartibiA03', 'TartibiA04', 'TartibiA05',\
                                                                                    'TartibiA13', 'TartibiA14', 'TartibiA15',\
                                                                                        'TartibiA24', 'TartibiA25',\
                                                                                            'TartibiA35',\
                                                                                                'TartibiA60','TartibiA61','TartibiA62','TartibiA63','TartibiA64',\
                                                                                                    'TartibiB02', 'TartibiB03', 'TartibiB04', 'TartibiB05',\
                                                                                                        'TartibiB13', 'TartibiB14', 'TartibiB15',\
                                                                                                            'TartibiB24','TartibiB25',\
                                                                                                                'TartibiB35',\
                                                                                                                    'TartibiB60','TartibiB61','TartibiB62','TartibiB63','TartibiB64',\
                                                                                                                    *RaghamAval, *RaghamDovom])

    #minusRoundType  = np.array(['SadSadi11', 'SadSadi22', '6raghamAvalYeki', '6raghamAkharYeki', '7raghamYeki', ])

    stringLenght_ = lambda x2: list(map(lambda x1: len(x1), allhow2read[x2]))
    all_StringLenght = list(map(lambda _: stringLenght_(_), range(len(allhow2read))))

    #all_StringLenght

    for i in range(len(all_StringLenght)):
            
        unique_stringLength, counts_stringLength = np.unique(all_StringLenght[i], return_counts=True)
        #print(allhow2read[i])
        #print(all_StringLenght[i])
        #usl =[]
        for j in range(len(unique_stringLength)):
                
            #wh2r = np.where(all_StringLenght[i] == unique_stringLength[j])# index oon do raghamiha chie
            #wh2r = wh2r[0]
            ih2r = allhow2read[i] # khode shomare chie 
            len_ih2r = len(ih2r)    
                
                    
            # Ayeneie ===================================================================        
            if unique_stringLength[j] == 2: # agar 2 raghami dashte bashim

                if counts_stringLength[j] == 2: # agar 2 ta bashan
                    if all_StringLenght[i] == [2, 2, 3]: # [2 2 3] , [3 2 2]ke do raghamiha faghat kenare ham aval bian ya akhar, va baghie raghamha ham baham khoonde shan, ayani faghat 3 ta jomle shan
                        if ih2r[0][0] != '0' and \
                            ih2r[0][0] != ih2r[0][1] and \
                            ih2r[0] == ''.join(np.flip([*ih2r[1]])): # 
                            #print('Ayeneie_21: ', ih2r, [0, 1])
                            feature_name['Ayeneie_21'] = ih2r
            
            
                    elif all_StringLenght[i] == [3, 2, 2]: # [2 2 3] , [3 2 2]ke do raghamiha faghat kenare ham aval bian ya akhar, va baghie raghamha ham baham khoonde shan, ayani faghat 3 ta jomle shan
                        if ih2r[1][0] != '0' and \
                            ih2r[1][0] != ih2r[1][1] and \
                            ih2r[1] == ''.join(np.flip([*ih2r[2]])): # 
                            #print('Ayeneie_22: ', ih2r, [1, 2])                         
                            feature_name['Ayeneie_22'] = ih2r
                            
                    elif all_StringLenght[i] == [2, 3, 2]:
                        if ih2r[0][0] != '0' and \
                            ih2r[0][0] != ih2r[0][1] and \
                            ih2r[0] == ''.join(np.flip([*ih2r[2]])):
                            #print('Ayeneie_23: ', ih2r, [0, 2])
                            feature_name['Ayeneie_23'] = ih2r
                            
            elif unique_stringLength[j] == 3: # agar 3 raghami dashte bashim  
                
                if counts_stringLength[j] == 2: # agar 2 ta bashan    
                    if  all_StringLenght[i] == [3, 1, 3]: # agar 2 ta bashan [3 1 3]
                        if ih2r[0][0] != '0' and \
                            ih2r[0] != ih2r[2] and \
                            ih2r[0] == ''.join(np.flip([*ih2r[2]])):
                            #print('Ayeneie_31: ', ih2r, [0, 2]) 
                            feature_name['Ayeneie_31'] = ih2r
                        
                    elif   all_StringLenght[i] == [3, 3, 1]: # agar 2 ta bashan [3 1 3]      
                        if ih2r[0][0] != '0' and \
                            ih2r[0] != ih2r[1] and \
                            ih2r[0] == ''.join(np.flip([*ih2r[1]])):
                            #print('Ayeneie_32: ', ih2r, [0, 2]) 
                            feature_name['Ayeneie_32'] = ih2r 
                    
                    elif   all_StringLenght[i] == [1, 3, 3]: # agar 2 ta bashan [3 1 3]      
                        if ih2r[1][0] != '0' and \
                            ih2r[1] != ih2r[2] and \
                            ih2r[1] == ''.join(np.flip([*ih2r[2]])):
                            #print('Ayeneie_33: ', ih2r, [1, 2]) 
                            feature_name['Ayeneie_33'] = ih2r 
                        
                        
            # Tarazuie  ===================================================================        
            if unique_stringLength[j] == 3: # agar 2 raghami dashte bashim
                if counts_stringLength[j] == 2: # agar 2 ta bashan
                    if  all_StringLenght[i] == [3, 1, 3]: # [3 1 3]
                        if ih2r[0] == ih2r[2]:
                            #print('Tarazuie: ', ih2r, [0, 2])     
                            feature_name['Tarazuie'] = ih2r
                    
                    
            # Pelie  ===================================================================   
            if  unique_stringLength[j] == 2:
                if counts_stringLength[j] == 2:
                    if all_StringLenght[i] == [2, 2, 3]: # az aval [2 2 3]
                        if (ih2r[0][0] == ih2r[1][0] or ih2r[0][1] == ih2r[1][1]) and \
                            ih2r[0] != ih2r[1] and (ih2r[0][1] != '0' and ih2r[1][1] != '0') and ih2r[0][1] != '0':
                            #print('Pleie21: ', ih2r, [0, 1])
                            feature_name['Pleie21'] = ih2r
                            
                    elif all_StringLenght[i] == [3, 2, 2]: # az akhar [3 2 2]
                        if (ih2r[1][0] == ih2r[2][0] or ih2r[1][1] == ih2r[2][1]) and \
                            ih2r[1] != ih2r[2] and ih2r[1][1] != '0':
                            #print('Pleie22: ', ih2r, [1, 2])
                            feature_name['Pleie22'] = ih2r
        
                elif counts_stringLength[j] == 3:
        
                    if all_StringLenght[i] == [1, 2, 2, 2]: # az aval [1 2 2 2]
                        if ((ih2r[1][0] == ih2r[2][0]) or (ih2r[1][1] == ih2r[2][1])) and \
                            ((ih2r[2][0] == ih2r[3][0]) or (ih2r[2][1] == ih2r[3][1])) and \
                                (ih2r[1] != ih2r[2] != ih2r[3]) and \
                                ih2r[1][1] !='0':
                            #print('Pleie31: ', ih2r, [1, 2, 3]) 
                            feature_name['Pleie31'] = ih2r
                            
                        elif ((ih2r[1][0] == ih2r[2][0]) or (ih2r[1][1] == ih2r[2][1])) and \
                            (ih2r[1] != ih2r[2]) and \
                                ih2r[1][0] !='0':         
                            #print('Pleie23: ', ih2r, [1, 2]) 
                            feature_name['Pleie23'] = ih2r
                            
                    elif all_StringLenght[i] == [2, 2, 2, 1]: 
                        if ((ih2r[0][0] == ih2r[1][0]) or (ih2r[0][1] == ih2r[1][1])) and \
                            ((ih2r[1][0] == ih2r[2][0]) or (ih2r[1][1] == ih2r[2][1])) and \
                                (ih2r[0] != ih2r[1] != ih2r[2]) and \
                                ih2r[0][1] !='0':
                                #print('Pleie32: ', ih2r, [0, 1, 2]) 
                                feature_name['Pleie32'] = ih2r
                            
                        elif ((ih2r[1][0] == ih2r[2][0]) or (ih2r[1][1] == ih2r[2][1])) and \
                            (ih2r[1] != ih2r[2]) and \
                                ih2r[1][0] !='0':         
                                #print('Pleie24: ', ih2r, [1, 2])     
                                feature_name['Pleie24'] = ih2r
                    elif all_StringLenght[i] == [2, 2, 1, 2]:  
                        if ih2r[2] == '0' and ((ih2r[1][0] == ih2r[3][0]) or (ih2r[1][1] == ih2r[3][1])) and \
                            ih2r[1] != ih2r[3]:
                                feature_name['Pleie25'] = ih2r
                        
                        
                        
                                                
            elif  unique_stringLength[j] == 3:
                if counts_stringLength[j] == 2:
                    if all_StringLenght[i] == [3, 3, 1]: # az aval [3 3 1]
                        if (ih2r[0][0:2] == ih2r[1][0:2] and ih2r[0][2] != ih2r[1][2]) or \
                            (ih2r[0][0] != ih2r[1][0] and ih2r[0][1:] == ih2r[1][1:]) and \
                                ih2r[0][1:] !='00':                                
                                #print('Pleie33: ', ih2r, [0, 1])  
                                feature_name['Pleie33'] = ih2r
                                
                    elif all_StringLenght[i] == [1, 3, 3]: # az aval [1 3 3]
                        if (ih2r[1][0:2] == ih2r[2][0:2] and ih2r[1][2] != ih2r[2][2]) or \
                            (ih2r[1][0] != ih2r[2][0] and ih2r[1][1:] == ih2r[2][1:]) and \
                                ih2r[1][1:] !='00':                                
                                #print('Pleie34: ', ih2r, [1, 2])           
                                feature_name['Pleie34'] = ih2r
            
            
            # Joft  ===================================================================   
            if  unique_stringLength[j] == 2:
                if counts_stringLength[j] == 2:
                    if all_StringLenght[i] == [2, 2, 3]: # az aval [2 2 3]
                        if ih2r[0][0] != '0' and ih2r[0] == ih2r[1]:  
                            #print('Joft21: ', ih2r, [0, 1])
                            feature_name['Joft21'] = ih2r
                            
                    elif  all_StringLenght[i] == [3, 2, 2]: # az akhar [3 2 2]
                        if ih2r[1][0] != '0' and ih2r[1] == ih2r[2]:  
                            #print('Joft22: ', ih2r, [1, 2])
                            feature_name['Joft22'] = ih2r
                            
                elif counts_stringLength[j] == 3:
                    if all_StringLenght[i] == [2, 2, 2, 1]: # az aval [2 2 2 1]
                        if ih2r[0][0] != '0' and ih2r[0] == ih2r[1] == ih2r[2]:  
                            #print('Joft23: ', ih2r, [0, 1, 2]) 
                            feature_name['Joft23'] = ih2r
                        
                        elif ih2r[0][0] != '0' and ih2r[1] == ih2r[2]: 
                            #print('Joft26: ', ih2r, [1, 2])   
                            feature_name['Joft26'] = ih2r                     
        
                    elif all_StringLenght[i] == [1, 2, 2, 2]: # az aval [1 2 2 2]
                        if ih2r[1][0] != '0' and ih2r[1] == ih2r[2] == ih2r[3]:
                            #print('Joft24: ', ih2r, [1, 2, 3]) 
                            feature_name['Joft24'] = ih2r 
                            
                        elif ih2r[1][0] != '0' and ih2r[1] == ih2r[2]:   
                            #print('Joft25: ', ih2r, [1, 2]) 
                            feature_name['Joft25'] = ih2r
        
            elif  unique_stringLength[j] == 3:
                if counts_stringLength[j] == 2:
                    if all_StringLenght[i] == [3, 3, 1]: # az aval [3 3 1]
                        if ih2r[0][0] != '0' and ih2r[0] == ih2r[1]:    
                            #print('Joft31: ', ih2r, [0, 1]) 
                            feature_name['Joft31'] = ih2r 
                    
                    elif all_StringLenght[i] == [1, 3, 3]: # az aval [1 3 3]
                        if ih2r[1][0] != '0' and ih2r[1] == ih2r[2]:    
                            #print('Joft32: ', ih2r, [1, 2])                  
                            feature_name['Joft32'] = ih2r 
                    
                    
            # DahDahi  =================================================================== 
            if  unique_stringLength[j] == 2:
                if counts_stringLength[j] == 2:
                    if all_StringLenght[i] == [2, 2, 3]: # az aval [2 2 3]
                        if ih2r[0][0] != '0' and ih2r[0][0] == ih2r[1][0] and ih2r[0][1] == '0' and ih2r[1][1] == '0':  
                            #print('DahDahi11: ', ih2r, [0, 1])
                            feature_name['DahDahi11'] = ih2r
                            
                        elif ih2r[0][0] != '0' and  ih2r[0][0] != ih2r[1][0] and ih2r[0][1] == '0' and ih2r[1][1] == '0':
                            #print('DahDahi12: ', ih2r, [0, 1])
                            feature_name['DahDahi12'] = ih2r
                            
                        elif ih2r[0][0] == '0' and ih2r[1][0] == '0' and ih2r[0][1] == ih2r[1][1] and ih2r[0][1] !='0':   
                            #print('DahDahi11: ', ih2r, [0, 1])
                            feature_name['DahDahi13'] = ih2r 
                            
                        elif ih2r[0][0] == '0' and ih2r[1][0] == '0' and ih2r[0][1] != ih2r[1][1] :  
                            #print('DahDahi12: ', ih2r, [0, 1])
                            feature_name['DahDahi14'] = ih2r   
                            
                    elif all_StringLenght[i] == [3, 2, 2]: # az aval [3 2 2]
                        if ih2r[1][0] != '0' and ih2r[1][0] == ih2r[2][0] and ih2r[1][1] == '0' and ih2r[2][1] == '0':  
                            #print('DahDahi21: ', ih2r, [1, 2])
                            feature_name['DahDahi21'] = ih2r
            
                        elif ih2r[1][0] != '0' and  ih2r[1][0] != ih2r[2][0] and ih2r[1][1] == '0' and ih2r[2][1] == '0':
                            #print('DahDahi22: ', ih2r, [1, 2])
                            feature_name['DahDahi22'] = ih2r
                            
                        elif  ih2r[1][0] == '0' and ih2r[2][0] == '0' and ih2r[1][1] == ih2r[2][1] and ih2r[1][1] !='0':  
                            #print('DahDahi21: ', ih2r, [1, 2])
                            feature_name['DahDahi23'] = ih2r
            
                        elif  ih2r[1][0] == '0' and ih2r[2][0] == '0' and ih2r[1][1] != ih2r[2][1] : 
                            #print('DahDahi22: ', ih2r, [1, 2])
                            feature_name['DahDahi24'] = ih2r   
                            
                                        
                elif counts_stringLength[j] ==3:   
                    if all_StringLenght[i] == [1, 2, 2, 2]:        
                        if ih2r[1][0] != '0' and ih2r[1][0] == ih2r[2][0] and ih2r[1][1] == '0' and ih2r[2][1] == '0':  
                            #print('DahDahi31: ', ih2r, [0, 1])
                            feature_name['DahDahi31'] = ih2r
                            
                        elif ih2r[1][0] != '0' and ih2r[1][0] != ih2r[2][0] and ih2r[1][1] == '0' and ih2r[2][1] == '0':         
                            #print('DahDahi32: ', ih2r, [0, 1])
                            feature_name['DahDahi32'] = ih2r
                            
                    elif all_StringLenght[i] == [2, 2, 2, 1]:
                        if ih2r[1][0] != '0' and ih2r[1][0] == ih2r[2][0] and ih2r[1][1] == '0' and ih2r[2][1] == '0':  
                            #print('DahDahi41: ', ih2r, [0, 1])
                            feature_name['DahDahi41'] = ih2r
                            
                        elif ih2r[1][0] != '0' and ih2r[1][0] != ih2r[2][0] and ih2r[1][1] == '0' and ih2r[2][1] == '0':         
                            #print('DahDahi42: ', ih2r, [0, 1])                    
                            feature_name['DahDahi42'] = ih2r
                        
                        
            # SadSadi  =================================================================== 
            if  unique_stringLength[j] == 3:
                if counts_stringLength[j] == 2:
                    if all_StringLenght[i] == [3, 3, 1]: # az aval [3 3 1]
                        if ih2r[0][0] == ih2r[1][0] and ih2r[0][1:] == '00' and ih2r[1][1:] == '00':  
                            #print('SadSadi11: ', ih2r, [0, 1])
                            feature_name['SadSadi11'] = ih2r
                            
                        elif ih2r[0][0] != ih2r[1][0] and ih2r[0][1:] == '00' and ih2r[1][1:] == '00':
                            #print('SadSadi12: ', ih2r, [0, 1])
                            feature_name['SadSadi12'] = ih2r
            
                    elif all_StringLenght[i] == [1, 3, 3]: # az aval [1 3 3]
                        if ih2r[1][0] == ih2r[2][0] and ih2r[1][1:] == '00' and ih2r[2][1:] == '00':  
                            #print('SadSadi21: ', ih2r, [1, 2])
                            feature_name['SadSadi21'] = ih2r
            
                        elif ih2r[1][0] != ih2r[2][0] and ih2r[1][1] == '00' and ih2r[2][1] == '00':
                            #print('SadSadi22: ', ih2r, [1, 2])            
                            feature_name['SadSadi22'] = ih2r 
            
            
            # CodeHezari  =================================================================== 
            if  unique_stringLength[j] == 4:
                if counts_stringLength[j] == 1:
                    if all_StringLenght[i] == [4, 3]: #  [4 3]            
                        if int(ih2r[0]) in list(range(1000,10000,1000)) and \
                            ih2r[1][0] != '0':
                            #print('CodeHezari11: ', ih2r, [0])  
                            feature_name['CodeHezari11'] = ih2r 
                    
                        elif int(ih2r[0]) in list(range(1500,10000,1000)) and \
                            ih2r[1][0] != '0':
                            #print('CodeHezari12: ', ih2r, [0])
                            feature_name['CodeHezari12'] = ih2r 
                        
                        elif ih2r[0][1:3] == '00' and ih2r[1][0] != '0':
                               feature_name['CodeHezari13'] = ih2r    
                               
                        elif  ih2r[0][2:] == '00' and ih2r[1][0] != '0':
                               feature_name['CodeHezari14'] = ih2r      
                    
                    elif all_StringLenght[i] == [3, 4]: # [3 4] 
                        if int(ih2r[1]) in list(range(1000,10000,1000)):
                            #print('CodeHezari21: ', ih2r, [1])
                            feature_name['CodeHezari21'] = ih2r 
                    
                        elif int(ih2r[1]) in list(range(1500,10000,1000)):
                            #print('CodeHezari22: ', ih2r, [1])
                            feature_name['CodeHezari22'] = ih2r
                       
                        elif ih2r[1][1:3] == '00' and ih2r[1][0] != '0':
                               feature_name['CodeHezari23'] = ih2r  
          
                        elif  ih2r[1][2:] == '00' and ih2r[1][0] != '0':
                               feature_name['CodeHezari24'] = ih2r                       
                                                    
        
            # CodeDahHezari  =================================================================== 
            if  unique_stringLength[j] == 5:
                if  counts_stringLength[j] == 1:                    
                    if  all_StringLenght[i] == [5, 2]: # az aval [5 2]            
                        if  int(ih2r[0]) in list(range(10000,100000,10000)) and \
                            ih2r[1][0] != '0':
                            #print('CodeDahHezari11: ', ih2r, [0])  
                            feature_name['CodeDahHezari11'] = ih2r
                        
                        elif int(ih2r[0]) in list(range(15000,100000,10000)) and \
                            ih2r[1][0] != '0':
                            #print('CodeDahHezari12: ', ih2r, [0]) 
                            feature_name['CodeDahHezari12'] = ih2r 
            
                    elif all_StringLenght[i] == [2, 5]: # az aval [2 5]            
                        if int(ih2r[1]) in list(range(10000,100000,10000)):
                            #print('CodeDahHezari21: ', ih2r, [1])   
                            feature_name['CodeDahHezari21'] = ih2r 
                    
                        elif int(ih2r[1]) in list(range(15000,100000,10000)):
                            #print('CodeDahHezari22: ', ih2r, [1])  
                            feature_name['CodeDahHezari22'] = ih2r 
            
            # CodeMiluni  =================================================================== 
            if  unique_stringLength[j] == 1:
                if counts_stringLength[j] == 7:
                    if len_ih2r == 7 : # az aval [1 1 1 1 1 1 1]            
                        unique_, counts_ = np.unique(ih2r[:], return_counts=True)
                        if (unique_ == '0').any():
                            wh2r_0 = np.where(unique_ == '0')
                            wh2r_0 = wh2r_0[0]
                            if unique_[wh2r_0[0]] == '0' and counts_[wh2r_0[0]] >= 5:
                                #print('CodeMiluni: ', ''.join(ih2r[:]), [0]) 
                                feature_name['CodeMiluni'] = ih2r 
        
        
            # az2adad  =================================================================== 
            if  unique_stringLength[j] == 1:
                if counts_stringLength[j] == 7:
                    if len_ih2r == 7 : # az aval [1 1 1 1 1 1 1]            
                        unique_ = np.unique(ih2r[:])
                        if len(unique_) == 2:
                            #print('az2adad: ', ''.join(ih2r[:]), [0])
                            feature_name['َAz2adad'] = ih2r 
        
        
            # NraghamAvalYeki  =================================================================== 
            # n: 3,4,5,6
            for r in range(0,4): 
                if  unique_stringLength[j] == 3+r:
                    if counts_stringLength[j] == 1:
                        if all_StringLenght[i] == [3+r, 7-3-r]:#[3 4] 
                            logiih2r = True
                            for h in range(0, len(ih2r[0])-1):          
                                logiih2r = logiih2r and  ih2r[0][h] == ih2r[0][h+1] 
                            
                            if logiih2r == True and ih2r[0][3+r-1] != ih2r[1][0]:
                                #print(f'{3+r}raghamAvalYeki: ', ih2r, [0])
                                feature_name[f'{3+r}raghamAvalYeki'] = ih2r 

        
            # NraghamAkharYeki  =================================================================== 
            # n: 3,4,5,6
            for r in range(0,4): 
                if  unique_stringLength[j] == 3+r:
                    if counts_stringLength[j] == 1:
                        if all_StringLenght[i] == [7-3-r, 3+r]:                        
                            ihtr_f = ''.join(np.flip([*ih2r[1]]))
                            logiih2r = True
                            for h in range(0, len(ihtr_f)-1):   
                            #print(ihtr_f)       
                                logiih2r = logiih2r and  ihtr_f[h] == ihtr_f[h+1] 
                            
                            if logiih2r == True and ihtr_f[-1] != ih2r[0][-1]:
                                #print(f'{3+r}raghamAkharYeki: ', ih2r, [1]) 
                                feature_name[f'{3+r}raghamAkharYeki'] = ih2r 
                    
                                
            # 7raghamYeki  =================================================================== 
            if len(ih2r) == 7 and ''.join(ih2r[:]) == 7*ih2r[0]:
                #print('7raghamYeki: ', ''.join(ih2r), [0]) 
                feature_name['7raghamYeki'] = ih2r


            # NraghamVasatYeki  =================================================================== 
            if unique_stringLength[j] == 3:
                if counts_stringLength[j] == 1:
                    if all_StringLenght[i] == [2, 3, 2]:
                        if ih2r[1] == 3*ih2r[1][0]: 
                            if ih2r[1][-1] != ih2r[2][0] and ih2r[1][0] != ih2r[0][-1]:
                                #print('3raghamVasatYeki: ', ih2r, [1]) 
                                feature_name['3raghamVasatYeki01'] = ih2r
                    elif  all_StringLenght[i] == [1, 3, 3]:
                        if ih2r[1] == 3*ih2r[1][0]: 
                            if ih2r[1][-1] != ih2r[2][0] and ih2r[1][0] != ih2r[0][-1]:
                                feature_name['3raghamVasatYeki02'] = ih2r
                    elif all_StringLenght[i] == [3, 3, 1]:         
                        if ih2r[2][0] == ih2r[2][1] == ih2r[2][2] and \
                            ih2r[3] != '000' :
                                feature_name['3raghamVasatYeki03'] = ih2r 
                            
            elif  unique_stringLength[j] == 4:
                if counts_stringLength[j] == 1:
                    if all_StringLenght[i] == [1, 4, 2]:              
                        if ih2r[1] == 4*ih2r[1][0]: 
                            if ih2r[1][-1] != ih2r[2][0] and ih2r[1][0] != ih2r[0][-1]:
                                #print('4raghamVasatYeki01: ', ih2r, [1]) 
                                feature_name['4raghamVasatYeki01'] = ih2r
                    
                    elif len_ih2r == 3 and all_StringLenght[i] == [2, 4, 1]:
                        if ih2r[1] == 4*ih2r[1][0]:
                            if ih2r[1][-1] != ih2r[2][0] and ih2r[1][0] != ih2r[0][-1]:
                                #print('4raghamVasatYeki02: ', ih2r, [1])
                                feature_name['4raghamVasatYeki02'] = ih2r
            
            elif  unique_stringLength[j] == 5:
                if counts_stringLength[j] == 1:
                    if all_StringLenght[i] == [1, 5, 1]:              
                        if ih2r[1] == 5*ih2r[1][0]: 
                            if ih2r[1][-1] != ih2r[2][0] and ih2r[1][0] != ih2r[0][-1]:
                                #print('5raghamVasatYeki: ', ih2r, [1])
                                feature_name['5raghamVasatYeki'] = ih2r
            
            
            # CodePaien  ===================================================================             
            if  unique_stringLength[j] == 3:
                if counts_stringLength[j] == 1:
                    if all_StringLenght[i] == [3, 2, 2]: # az aval [3 2 2]            
                        if int(ih2r[0]) in list(range(100,120)):
                            #print('CodePaien1: ', ih2r, [0]) 
                            feature_name['CodePaien1'] = ih2r            
                    
                        elif int(ih2r[0]) in list(range(200,220)):
                            #print('CodePaien2: ', ih2r, [0])
                            feature_name['CodePaien2'] = ih2r  
                                                                
                        elif int(ih2r[0]) in list(range(300,320)):
                            #print('CodePaien3: ', ih2r, [0])   
                            feature_name['CodePaien3'] = ih2r 
                        
                        elif int(ih2r[0]) in list(range(400,420)):
                            #print('CodePaien4: ', ih2r, [0])  
                            feature_name['CodePaien4'] = ih2r 
                        
                        elif int(ih2r[0]) in list(range(500,520)):
                            #print('CodePaien4: ', ih2r, [0])  
                            feature_name['CodePaien5'] = ih2r                         
            
            # TarikhTavalod_shamsi  =================================================================== 
            if  unique_stringLength[j] == 4:
                if counts_stringLength[j] == 1:
                    if all_StringLenght[i] == [4, 3]: # az aval [3 2 2]            
                        
                        if int(ih2r[0]) in list(range(1300,1405)):
                            #print('TarikhTavalodS1: ', ih2r, [0]) 
                            feature_name['TarikhTavalodS1'] = ih2r 
                            
                        elif  int(ih2r[0]) in list(range(1928,2030)):                    
                            #print('TarikhTavalodM1: ', ih2r, [0]) 
                            feature_name['TarikhTavalodM1'] = ih2r 
                            
                    elif all_StringLenght[i] == [3, 4]: # az aval [3 2 2] 
                        
                        if int(ih2r[1]) in list(range(1300,1405)):
                            #print('TarikhTavalodS2: ', ih2r, [0])
                            feature_name['TarikhTavalodS2'] = ih2r 
                                                        
                        elif  int(ih2r[1]) in list(range(1928,2030)):                    
                            #print('TarikhTavalodM2: ', ih2r, [0])
                            feature_name['TarikhTavalodM2'] = ih2r
                                            
                                                        
            # PishShomre  ===================================================================  
            if  unique_stringLength[j] == 4:
                if counts_stringLength[j] == 1:
                    if all_StringLenght[i] == [4, 3]: # az aval [3 2 2]            
                        if int(ih2r[0]) in ['0912','0935','0910','0902','0098','0903','0921']:
                            #print('PishShomreA01: ', ih2r, [0]) 
                            feature_name['PishShomreA01'] = ih2r
                                                        
                    elif all_StringLenght[i] == [3, 4]: # az aval [3 2 2]     
                        if int(ih2r[1]) in ['0912', '0935', '0910', '0902','0098']:
                            #print('PishShomreA02: ', ih2r, [0])
                            feature_name['PishShomreA02'] = ih2r
        
            elif  unique_stringLength[j] == 3: 
                if counts_stringLength[j] == 1:
                    if all_StringLenght[i] == [3, 2, 2]: # az aval [3 2 2]                     
                        if int(ih2r[0]) in ['021', '118', '119', '110', '125']:
                            #print('PishShomreB01: ', ih2r, [0]) 
                            feature_name['PishShomreB01'] = ih2r
                            
                    elif all_StringLenght[i] == [2, 2, 3]: # az aval [3 2 2]     
                        if int(ih2r[2]) in ['021', '118', '119', '110', '125']:
                            #print('PishShomreB02: ', ih2r, [0])
                            feature_name['PishShomreB02'] = ih2r
                        

            # Tartibi  ===================================================================         
            if len(ih2r) == 7: 
                num = np.array(ih2r).astype(int)            
                
                #[print(f'Tartibi0{i}: ', ih2r, [0]) for i in range(2,7) if sumCheck_(0,i) and not sumCheck_(0,i+1)] 
                
                sumCheckA_ = lambda i1,i2: num[i2] * (num[i2]+1) * 0.5 - (num[i1]-1) * (num[i1]-1+1) * 0.5 == num[i1:(i2+1)].sum() != 0 and \
                    0 not in num[i1:(i2+1)] and \
                        (np.diff(num[i1:i2]) > 0).all()
                        
                #if sumCheckA_(0,6):
                #    print(f'TartibiA0{7}: ', ''.join(ih2r[0:]), [0])            
                #else:
                    #whilebreak = False 
                    #while True:
                for i in range(2, 6):
                    if sumCheckA_(0, i) and not sumCheckA_(0, i+1):
                        #print(f'TartibiA0{i}: ', [''.join(ih2r[0:i+1]), ''.join(ih2r[i+1:])], [0]) 
                        feature_name[f'TartibiA0{i}'] = [''.join(ih2r[0:i+1]), ''.join(ih2r[i+1:])]  
                        #whilebreak = True               
                        #break
                #if whilebreak: break
                
                for i in range(3, 6):
                    if sumCheckA_(1, i) and not sumCheckA_(1, i+1):
                        #print(f'TartibiA1{i}: ', [ih2r[0], ''.join(ih2r[1:i+1]), ''.join(ih2r[i+1:])], [0])
                        feature_name[f'TartibiA1{i}'] = [ih2r[0], ''.join(ih2r[1:i+1]), ''.join(ih2r[i+1:])]
                        #whilebreak = True               
                        #break
                #if whilebreak: break  
                
                for i in range(4, 6):
                    if sumCheckA_(2,i) and not sumCheckA_(2, i+1):
                        #print(f'TartibiA2{i}: ', [''.join(ih2r[0:2]), ''.join(ih2r[2:i+1]), ''.join(ih2r[i+1:])], [0])
                        feature_name[f'TartibiA2{i}'] = [''.join(ih2r[0:2]), ''.join(ih2r[2:i+1]), ''.join(ih2r[i+1:])] 
                        #whilebreak = True               
                        #break
                #if whilebreak: break               
            
                for i in range(5,6):
                    if sumCheckA_(3,i) and not sumCheckA_(3, i+1):
                        #print(f'TartibiA3{i}: ', [''.join(ih2r[0:3]), ''.join(ih2r[3:i+1]), ''.join(ih2r[i+1:])], [0])
                        feature_name[f'TartibiA3{i}'] = [''.join(ih2r[0:3]), ''.join(ih2r[3:i+1]), ''.join(ih2r[i+1:])]
                        #whilebreak = True               
                        #break
                    
                for ii in range(0, 5):                        
                    if sumCheckA_(ii, 6): #and not sumCheckA_(3, i+1):
                        #print(f'TartibiA{ii}6: ', [''.join(ih2r[0:ii]), ''.join(ih2r[ii:])], [0])
                        feature_name[f'TartibiA6{ii}'] = [''.join(ih2r[0:ii]), ''.join(ih2r[ii:])]
                        #whilebreak = True  
                        #break
                                                                                            
                #if whilebreak: break
                #break                
                    
                sumCheckB_ = lambda i1,i2: num[i1] * (num[i1]+1) * 0.5 - (num[i2]-1) * (num[i2]-1+1) * 0.5 == num[i1:(i2+1)].sum() !=0 and \
                    0 not in num[i1:(i2+1)] and \
                        (np.diff(num[i1:i2]) < 0).all()
                        
                #if sumCheckB_(0,6):
                #    print(f'TartibiB0{7}: ', [''.join(ih2r[0:])], [0])           
                #else:
                    #whilebreak = False 
                    #while True:
                for i in range(2,6):
                    if sumCheckB_(0,i) and not sumCheckB_(0, i+1):
                        #print(f'TartibiB0{i}: ', [''.join(ih2r[0:i+1]), ''.join(ih2r[i+1:])], [0])  
                        feature_name[f'TartibiB0{i}'] = [''.join(ih2r[0:i+1]), ''.join(ih2r[i+1:])]
                        #whilebreak = True               
                        #break
                #if whilebreak: break
                        
                for i in range(3,6):
                    if sumCheckB_(1,i) and not sumCheckB_(1, i+1):
                        #print(f'TartibiB1{i}: ', [ih2r[0], ''.join(ih2r[1:i+1]), ''.join(ih2r[i+1:])], [0])
                        feature_name[f'TartibiB1{i}'] = [ih2r[0], ''.join(ih2r[1:i+1]), ''.join(ih2r[i+1:])]
                        #whilebreak = True               
                        #break
                #if whilebreak: break  
                
                for i in range(4,6):
                    if sumCheckB_(2,i) and not sumCheckB_(2, i+1):
                        #print(f'TartibiB2{i}: ', [''.join(ih2r[0:2]), ''.join(ih2r[2:i+1]), ''.join(ih2r[i+1:])], [0])
                        feature_name[f'TartibiB2{i}'] = [''.join(ih2r[0:2]), ''.join(ih2r[2:i+1]), ''.join(ih2r[i+1:])]
                        #whilebreak = True               
                        #break
                #if whilebreak: break               
            
                for i in range(5,6):
                    if sumCheckB_(3,i) and not sumCheckB_(3, i+1):
                        #print(f'TartibiB3{i}: ', [''.join(ih2r[0:3]), ''.join(ih2r[3:i+1]), ''.join(ih2r[i+1:])], [0])
                        feature_name[f'TartibiB3{i}'] = [''.join(ih2r[0:3]), ''.join(ih2r[3:i+1]), ''.join(ih2r[i+1:])]
                        #whilebreak = True               
                        #break
                    
                for ii in range(0, 5):                        
                    if sumCheckB_(ii, 6): #and not sumCheckA_(3, i+1):
                        #print(f'TartibiB{ii}6: ', [''.join(ih2r[0:ii]), ''.join(ih2r[ii:])], [0])
                        feature_name[f'TartibiB6{ii}'] = [''.join(ih2r[0:ii]), ''.join(ih2r[ii:])]
                        #whilebreak = True  
                        #break                           
                    
                    
                #if whilebreak: break
                #break
            
            
            # doRaghamYeki  ===================================================================
            if  unique_stringLength[j] == 2:
                if counts_stringLength[j] == 2:
                
                    if all_StringLenght[i] == [3, 2, 2]: # az aval [3 2 2]        
                        if (ih2r[1][0] == ih2r[1][1] and ih2r[2][0] == ih2r[2][1]) and \
                            ih2r[1] != ih2r[2] and (ih2r[1] != '00' or ih2r[2] != '00'):
                            #print('doRaghamYeki2: ', ih2r, [0])
                            feature_name['doRaghamYeki21'] = ih2r
                   
                    elif all_StringLenght[i] == [2, 2, 3]: # az akhar [2 2 3]        
                        if (ih2r[0][0] == ih2r[0][1] and ih2r[1][0] == ih2r[1][1]) and \
                            ih2r[0] != ih2r[1] and (ih2r[0] != '00' or ih2r[1] != '00'):
                            feature_name['doRaghamYeki22'] = ih2r     
                            
                elif counts_stringLength[j] == 3:
                    if all_StringLenght[i] == [1, 2, 2, 2]: # az aval [3 2 2]        
                        if (ih2r[1][0] == ih2r[1][1] and ih2r[2][0] == ih2r[2][1] and ih2r[3][0] == ih2r[3][1] )and \
                            (ih2r[1] != ih2r[2] and ih2r[2] != ih2r[3] ) and (ih2r[1] != '00' or ih2r[2] != '00' or ih2r[3] != '00'):
                            #print('doRaghamYeki3: ', ih2r, [0])
                            feature_name['doRaghamYeki23'] = ih2r
                    elif all_StringLenght[i] == [2, 2, 2, 1]: # az aval [2 2 2 1]        
                        if (ih2r[0][0] == ih2r[0][1] and ih2r[1][0] == ih2r[1][1] and ih2r[2][0] == ih2r[2][1] )and \
                            (ih2r[0] != ih2r[1] and ih2r[1] != ih2r[2] ) and (ih2r[0] != '00' or ih2r[1] != '00' or ih2r[2] != '00'):
                            #print('doRaghamYeki3: ', ih2r, [0])
                            feature_name['doRaghamYeki24'] = ih2r
                   
                    elif all_StringLenght[i] == [1, 2, 2, 2]: # az aval [3 2 2]        
                        if (ih2r[1][0] == ih2r[1][1] and ih2r[2][0] == ih2r[2][1] )and \
                            (ih2r[1] != ih2r[2] ) and (ih2r[1] != '00' or ih2r[2] != '00'):
                            #print('doRaghamYeki3: ', ih2r, [0])
                            feature_name['doRaghamYeki25'] = ih2r
                            
                    elif all_StringLenght[i] == [2, 2, 2, 1]: # az aval [2 2 2 1]        
                        if (ih2r[1][0] == ih2r[1][1] and ih2r[2][0] == ih2r[2][1] )and \
                            (ih2r[1] != ih2r[2] ) and (ih2r[1] != '00' or ih2r[2] != '00'):
                            #print('doRaghamYeki3: ', ih2r, [0])
                            feature_name['doRaghamYeki26'] = ih2r
                                            
                            
            # CodeRiz  ===================================================================        
            if len(ih2r) == 7: 
                num = np.array(ih2r).astype(int)    
                if (num < 5).all():
                    #print('CodeRiz: ', ih2r, [0,1,2,3,4,5,6]) 
                    feature_name['CodeRiz'] = ih2r
                    
            # raghamAval  ===================================================================  
            # raghamDovom  ===================================================================           
            if  unique_stringLength[j] == 1:           
                if counts_stringLength[j] == 2:
                    if all_StringLenght[i] == [1, 1, 5]:                     
                        feature_name[f'RaghamAval{int(ih2r[0])}'] = ih2r
                        feature_name[f'RaghamDovom{int(ih2r[1])}'] = ih2r     
         
        keys = list(feature_name.keys())
        if len(keys) !=0:                               
            for i in range(len(keys)):
                if keys[i] in roundType:
                    idx = np.where(keys[i] == roundType)
                    #print(idx)
                    feature_vector[idx] = 1
                                               
                   
    return feature_name, feature_vector.reshape(1,len(roundType))

mlp_reg = pickle.load(open('phoneNumberPredict_model.sav', 'rb'))
def predictPrice(phoneNumber):
    featureDict, featureVector = RoundFeatures(phoneNumber)
    return featureDict, np.exp(mlp_reg.predict(featureVector.reshape(1,139)))

predictPrice_=lambda phoneNumber: predictPrice(phoneNumber,mlp_reg)