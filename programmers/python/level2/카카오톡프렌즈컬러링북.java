class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        int[][] checklist;
        int now = picture[0][0];
        int row = 0;
        int col = 0;
        while(0){
            picture[col-1][row];//상
            picture[col][row+1];//하
            picture[col+1][row];//좌
            picture[col][row-1];//우
            
            
            
        }
        return answer;
    }
}