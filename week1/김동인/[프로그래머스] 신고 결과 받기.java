import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int[] solution(String[] id_list, String[] reports, int k) {
        int[] result = new int[id_list.length];


        Map<String, Set<String>> relation = new HashMap<>();
        Set<String> blackSet = filteredBlackSet(reports, k, relation);

        for (int i = 0; i < id_list.length; i++) {
            String id = id_list[i];
            Set<String> reported = relation.get(id) == null ? new HashSet<>() : relation.get(id);
            Set<String> removed = new HashSet<>();
            for (String black : reported) {
                if (!blackSet.contains(black)) {
                    removed.add(black);
                }
            }
            reported.removeAll(removed);
            result[i] = relation.containsKey(id) ? relation.get(id).size() : 0;
        }

        return result;
    }

    private static Set<String> filteredBlackSet(String[] reports, int k, Map<String, Set<String>> relation) {
        Map<String, Integer> blackList = new HashMap<>();
        Set<String> alreadyReport = new HashSet<>();
        for (String report : reports) {
            // 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
            if (!alreadyReport.contains(report)) {
                String black = report.split(" ")[1];
                blackList.put(black, blackList.containsKey(black) ? blackList.get(black) + 1 : 1);
                alreadyReport.add(report);
            }

            String reporter = report.split(" ")[0];
            if (!relation.containsKey(reporter)) {
                relation.put(reporter, new HashSet<>());
            }
            relation.get(reporter).add(report.split(" ")[1]);
        }


        Set<String> blackSet = new HashSet<>();
        blackList.forEach((black, score) -> {
            // k번 이상 신고된 유저는 게시판 이용이 정지된다.
            if (score >= k) {
                blackSet.add(black);
            }
        });
        return blackSet;
    }
}
