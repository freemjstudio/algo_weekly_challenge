import java.util.PriorityQueue;

class Solution {

    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        for (int value: scoville) {
            priorityQueue.offer(value);
        }

        int count = 0;
        while (priorityQueue.peek() < K && priorityQueue.size() >= 2) {
            int swap = swap(priorityQueue.poll(), priorityQueue.poll());
            priorityQueue.offer(swap);
            count++;
        }

        if (priorityQueue.peek() < K) {
            return -1;
        }

        return count;
    }

    /**
     * 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
     */
    private int swap(int lowest, int second) {
        return lowest + (second * 2);
    }
}