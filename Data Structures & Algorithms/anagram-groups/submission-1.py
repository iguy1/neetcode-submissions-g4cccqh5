class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
            #if sorted word is equal to another sorted word we put them into a new subarray
            #we do this over and over again until all of the sorted words that match another word
            #Are in the same subarrays
            #then we put them back together and they are in the same subarray
        groups = {}

        for word in strs:
            #Creates the key
            sorted_word = "".join(sorted(word))

            #if the key is not there yet, we create an array for it
            if sorted_word not in groups:
                groups[sorted_word] = []
            
            #add the original word to the correct group

            groups[sorted_word].append(word)

        #lastly we return the values from the list we created
        return list(groups.values())
        
