import logging
from datetime import datetime

# Here we create name for our log file 
now = datetime.now()
fn_string = now.strftime("%d%m%Y%H%M%S")

# Here we create log file
logging.basicConfig(filename=f'.\\logs\\{fn_string}.log', level=logging.INFO)

class chamber:
    '''
    Chamber class containing the information about whether chamber is full, it's key and what is the next chamber
    init arguments:
    --------------
    key_value : int
        int value of the key
    '''
    def __init__(self, key_value):
        self.__key = key_value
        self.__next = None
        self.__full = False

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key_value):
        self.__key = key_value

    @property
    def full(self):
        return self.__full

    @full.setter
    def full(self, bool_value):
        if not isinstance(bool_value, bool):
            raise TypeError('Wrong value type')
        
        self.__full = bool_value
        return self.__full

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, element):
        self.__next = element

    def __repr__(self):
        return (f'<chamber with key {self.key}>')


class heart:
    '''
    Heart class containg 4 different chambers, information about blood circulations systems and values for electrocardiogram plot
    '''
    def __init__(self):
        # Here we create 4 chambers and link them to each other
        self.right_atrium = chamber(1)
        self.right_ventricle = chamber(2)
        self.right_atrium.next = self.right_ventricle
        self.left_atrium = chamber(3)
        self.right_ventricle.next = self.left_atrium
        self.left_ventricle = chamber(4)
        self.left_atrium.next = self.left_ventricle
        self.left_ventricle.next = self.right_atrium
        
        # Here we create siplified models of blood sirculation systems
        self.systemic_circulation = [0 for i in range(100000)]
        self.pulmonary_circulation = [0 for i in range(100)]

        # Here we create list for EKG signals values with 4 zeros at the begining        
        self.ekg = [0 for i in range(4)]

    def heart_beat(self):
        '''
        Function which simulates 2 contractions of the heart - atrial and vernicular
        '''
        for i in range(2):
            self.contraction()

    def contraction(self):
        '''
        Function which simulates the contraction of 2 chambers simultaneously, depending on in which chamber the blood is
        '''
        if self.right_atrium.full == 1 and self.left_atrium.full == 1:
            # Here we pass blood from atriums to verniciles by simulating atrial contraction
            self.blood_flow(self.right_atrium)
            self.blood_flow(self.left_atrium)
            logging.info('atriums contraction')
            # Here we append values of EKG signal
            for i in range(3):
                self.ekg.append(0.5)
            for i in range(4):
                self.ekg.append(0)

        elif self.right_ventricle.full == 1 and self.left_ventricle.full == 1:
            # Here we simulate vernicular contraction
            self.ekg.append(-0.3)
            self.blood_flow(self.right_ventricle)
            self.blood_flow(self.left_ventricle)
            logging.info('verniciles contraction')
            self.ekg.append(3)
            self.ekg.append(-0.3)
            for i in range(5):
                self.ekg.append(0)
            

    def blood_flow(self, chamber):
        '''
        Function which simulates the blood flow between chambers. If it's from atrium to vernicile it flows directly. If its from vernicile to atrium it first go through
        the blood circulation system

        Atributes:
        ----------
        chamber : chamber
            chamber object
        '''
        logging.info(f'blood in {chamber}')
        if chamber.full == True:
            # Here we handle flow from atrium to vernicile
            if chamber.next.key != 3 or chamber.next.key != 1:
                chamber.full = False
                chamber.next.full = True

        
            if chamber.next.key == 3:
                # Here we handle flow from right vernicile to left atrium through pulmonary circulation
                for i in range(len(self.pulmonary_circulation)):
                    self.pulmonary_circulation[i] = 1

                for i in range(len(self.pulmonary_circulation)):
                    self.pulmonary_circulation[i] = 0

                # if 1 not in self.pulmonary_circulation: print('pulmonary circulation ended')
                chamber.full = False
                chamber.next.full = True

            if chamber.next.key == 1:
                # Here we handle flow from left vernicile to right atrium through systemic circulation
                for i in range(len(self.systemic_circulation)):
                    self.systemic_circulation[i] = 1
                
                for i in range(len(self.systemic_circulation)):
                    self.systemic_circulation[i] = 0
                
                # if 1 not in self.systemic_circulation: print('systemic circulation ended')
                chamber.full = False
                chamber.next.full = True

        else: chamber = chamber.next
