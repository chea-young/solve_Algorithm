package java;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;


class Failure {
    public static void main(String args[]){
		Failure m1 = new Failure();
		int [] m1_list ={2, 1, 2, 6, 2, 4, 3, 3};
		for (int a: m1.solution(5, m1_list)) {
        	System.out.print(a+" ");
        }
        System.out.println("------------ 1 ");
		
        Failure m2 = new Failure();
        int [] m2_list ={4,4,4,4,4};
        for (int b: m2.solution(4, m2_list)) {
        	System.out.print(b+" ");
        }
        System.out.println("------------ 2 ");
	}

    public int[] solution(int N, int[] stages) {
        float[] n_clear = new float[N];
        float[] r_user = new float[N];
        float[][] answer = new float[N][2];
        for (int i=0; i<stages.length; i++){
            if(stages[i] == N+1){
                for (int j=0; j<N;j++){
                    r_user[j]++;
                }
                continue;
            }
            n_clear[stages[i]-1]++;
            for (int j=0; j<stages[i];j++){
                r_user[j]++;
            }
        }

        for(int i=0; i<N; i++){
            answer[i][0] = n_clear[i]/r_user[i];
            answer[i][1] = -(i+1);
        }

        Arrays.sort(answer, new Comparator<float[]>(){
            @Override
            public int compare(float[] t1, float[] t2){
                return (int)(t2[0]*100000000 - t1[0]*100000000);
            }
        });

        int[] answers = new int[N];
        for(int i=0; i<N; i++){
            answers[i] = -(int)answer[i][1];
        }
        return answers;
    }
}


