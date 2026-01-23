class Solution(object):

    def reverseRow(self,row):
        left = 0
        right = len(row)-1

        while(left < right):
            row[left],row[right] = row[right],row[left]
            left += 1
            right -= 1
        return row    

    def flipAndInvertImage(self, image):

        for row in image:
            self.reverseRow(row)
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] = 1-image[i][j]
        return image            
        

       
        