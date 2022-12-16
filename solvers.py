import time
class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # You should keep updating following variable with best string so far.
        self.best_state = None
    # def make_best_state(self,state):
    #     self.best_state = state

    def search(self, start_state):
        beam_number = 26
        self.best_state = start_state
        start_cost = self.cost_fn(start_state)
        curr_cost = start_cost
        best_cost = start_cost
        curr_state = start_state
        corr_chars = {}
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in alphabets :
            corr_chars[i] = []
        for i in alphabets:
            ch_list = self.conf_matrix[i]
            for j in range(0,len(ch_list)):
                ch = ch_list[j]
                corr_list = corr_chars[ch]
                corr_list.append(i)
                corr_chars[ch]= corr_list
                
        list_states = []
        list_states.append(start_state)
        #list_states.append(self.best_state)
        new_liststates = []
        while 1:
            for temp_state in list_states:
                k=0
                for i in temp_state:
                    if (i!=' ') and (i!='\n'):
                        list_corr= corr_chars[i]
                        for j in range(len(list_corr)):
                            curr_state = temp_state[:k] + list_corr[j] + temp_state[k+1:]
                            curr_cost = self.cost_fn(curr_state)
                            new_liststates.append((curr_cost, curr_state))
                    k=k+1

            list_states.clear()
            counter = min(beam_number, len(new_liststates))

            new_liststates.sort(key = lambda x: x[0])
            curr_cost = new_liststates[0][0]
            if(curr_cost<best_cost):
                self.best_state = new_liststates[0][1]
                best_cost = curr_cost
            for i in range(counter):
                list_states.append(new_liststates[i][1])
            new_liststates.clear()
            # print(self.best_state)
        
        raise Exception("Not Implemented.")
