class Solution {
    public boolean isPalindrome(ListNode head) {
            ListNode fastRunner = head;
            ListNode slowRunner = head;

            // O(N)
            // fastRunner == null 이면 짝수개
            // slowRunner.next == null 이면 홀수개
            while (fastRunner != null && fastRunner.next != null) {
                // fast runner
                fastRunner = fastRunner.next.next;
                // slow runner
                slowRunner = slowRunner.next;
            }

            // 홀수 개일 때 느린 러너가 한 칸 더 앞으로 가도록 처리
            if (fastRunner != null) {
                slowRunner = slowRunner.next;
            }

            // 중간에 도달한 느린 러너를 기준으로 역순 연결 리스트를 만든다.
            ListNode rev = null;
            while (slowRunner != null) {
                // 느린 러너로 역순 연결 리스트 rev를 만들어나간다.
                ListNode next = slowRunner.next;
                slowRunner.next = rev;
                rev = slowRunner;
                slowRunner = next;
            }

            while (rev != null) {
                // 역순 연결 리스트 rev와 기존 연결 리스트 head를 차례대로 비교
                if (rev.val != head.val) {
                    return false;
                }
                rev = rev.next;
                head = head.next;
            }
            return true;
    }
}
