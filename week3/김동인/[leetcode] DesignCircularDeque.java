/**
 * @see <a href="https://leetcode.com/problems/design-circular-deque/">Design Circular Deque</a>
 * 다음 연산을 제공하는 원형 데크를 디자인하라.
 *
 * - MyCircularDeque(k): 데크 크기를 k로 지정하는 생성자다.
 * - insertFront(): 데크 처음에 아이템을 추가하고 성공할 경우 true를 리턴한다.
 * - insertLast(): 데크 마지막에 아이템을 추가하고 성공할 경우 true를 리턴한다.
 * - deleteFront(): 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
 * - deleteLast(): 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
 * - getFront(): 데크의 첫 번째 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
 * - getRear(): 데크의 마지막 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
 * - isEmpty(): 데크가 비어 있는지 여부를 판별한다.
 * - isFull(): 데크가 가득 차 있는지 여부를 판별한다.
 */
public class DesignCircularDeque {
    public static void main(String[] args) {
        MyCircularDeque obj = new MyCircularDeque(3);
        boolean param_1 = obj.insertFront(1);
        boolean param_2 = obj.deleteLast();
        int param_3 = obj.getRear();
        int param_4 = obj.getFront();
        int param_5 = obj.getFront();
        boolean param_6 = obj.deleteFront();
        boolean param_7 = obj.insertFront(6);
        boolean param_8 = obj.insertLast(5);
        boolean param_9 = obj.insertFront(9);
        int param_10 = obj.getFront();
        boolean param_11 = obj.insertFront(6);
    }

    static class MyCircularDeque {
        int maxSize;
        LinkedList<Integer> linkedList = new LinkedList<>();

        public MyCircularDeque(int k) {
            this.maxSize = k;
        }

        public boolean insertFront(int value) {
            if (linkedList.size() == maxSize) {
                return false;
            }
            linkedList.addFirst(value);
            return true;
        }

        public boolean insertLast(int value) {
            if (linkedList.size() == maxSize) {
                return false;
            }
            linkedList.addLast(value);
            return true;
        }

        public boolean deleteFront() {
            if (linkedList.isEmpty()) {
                return false;
            }
            linkedList.removeFirst();
            return true;
        }

        public boolean deleteLast() {
            if (linkedList.isEmpty()) {
                return false;
            }
            linkedList.removeLast();
            return true;
        }

        public int getFront() {
            if (linkedList.isEmpty()) {
                return -1;
            }
            return linkedList.getFirst();
        }

        public int getRear() {
            if (linkedList.isEmpty()) {
                return -1;
            }
            return linkedList.getLast();
        }

        public boolean isEmpty() {
            return linkedList.isEmpty();
        }

        public boolean isFull() {
            return linkedList.size() == maxSize;
        }
    }
}
