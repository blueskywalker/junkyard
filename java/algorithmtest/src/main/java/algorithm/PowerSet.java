package algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collector;
import java.util.stream.Collectors;

/**
 * Created by jerrykim on 12/8/16.
 */
public class PowerSet {

    public static List<List<Integer>> perm(List<Integer> input) {
        ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();

        if (input.size()==0)
            return result;

        if (input.size()==1) {
            result.add(input);
            return result;
        }

        Integer head = input.get(0);
        List<List<Integer>> subResult = perm(input.subList(1,input.size()));
        for(List<Integer> elem : subResult) {
            for (int i = 0; i < input.size(); i++) {
                List<Integer> tmp = new ArrayList<Integer>(elem.subList(0, i));
                tmp.add(head);
                tmp.addAll(elem.subList(i,elem.size()));
                result.add(tmp);
            }
        }
        return result;
    }

    public static List<List<Integer>> subsets(List<Integer> input) {
        ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        result.add(new ArrayList<Integer>());

        for(Integer i : input) {
            ArrayList<List<Integer>> tmpList = new ArrayList<List<Integer>>();

            for(List<Integer> elem : result) {
                List<Integer> tmp = new ArrayList<Integer>(elem);
                tmp.add(i);
                tmpList.add(tmp);
            }
            result.addAll(tmpList);
        }
        return result;
    }


    public static void main(String[] args) {

        List<Integer> input = Arrays.asList(1,2,3);

        System.out.println(PowerSet.subsets(input));
        System.out.println(PowerSet.perm(input));

    }

}
