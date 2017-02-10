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
    final List<Integer> input;

    public PowerSet(List<Integer> input) {
        this.input = input;
    }

    public List<List<Integer>> subsets() {
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
        PowerSet power = new PowerSet(input);

        System.out.println(power.subsets());

    }

}
