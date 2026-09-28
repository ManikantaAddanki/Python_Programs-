"26/9/2026"


# class india:
#     def n_language(self):
#         print('india n_langauge Hindi')
        
#     def capital(self):
#         print('----india Capital Delhi---')
        
# class America:
#     def n_language(self):
#         print('America n_langauge English')
            
#     def capital(self):
#         print('----America Capital washington dc---')
        
# def Duck(n):   #  i_obj
#     n.n_language()
#     n.capital()
    
# i_obj = india()
# Duck(i_obj)

# print()
# a_obj = America()
# Duck(a_obj)
    
    
    
# import os
# from gtts import gTTS
# import time

# class UPI:
#     def pay(self,Amount):
        
#         tem = f"మీకు UPI  {Amount}  రూపాయలు విజయవంతంగా అందాయి. ట్రాన్సాక్షన్ పూర్తయింది."
        
#         s = gTTS(text=tem)
#         s.save('102.mp3')
#         os.startfile('102.mp3')
        
# class creditcard:
#     def pay(self,Amount):
#         tem = f"మీకు creditcard  {Amount}  రూపాయలు విజయవంతంగా అందాయి. ట్రాన్సాక్షన్ పూర్తయింది."
                
#         s = gTTS(text=tem)
#         s.save('102.mp3')
#         os.startfile('102.mp3')
        
# class phonepe:
#      def pay(self,Amount):
#         tem = f"మీకు phonepe  {Amount}  రూపాయలు విజయవంతంగా అందాయి. ట్రాన్సాక్షన్ పూర్తయింది."
                
#         s = gTTS(text=tem)
#         s.save('102.mp3')
#         os.startfile('102.mp3')
        
# def Duck(n,m):
#     n.pay(m)
    
# obj = [UPI(),creditcard(),phonepe()]
# a  = [5000,10000,5600]

# for x,y in zip(obj,a):
#     Duck(x,y)
#     time.sleep(7)
    

from gtts import gTTS  
import time
import os
        
        
class dog:
    def sound(self):
        tem = 'Bow Bow'
        s = gTTS(text=tem)
        s.save('102.mp3')
        for x in range(3):
            os.startfile('102.mp3')

class cat:
    def sound(self):
        tem = 'meow meow'
        s = gTTS(text=tem)
        s.save('102.mp3')
        for x in range(3):
            os.startfile('102.mp3')
            
def Duck(a):
    a.sound()
    
d_obj = cat()
Duck(d_obj)