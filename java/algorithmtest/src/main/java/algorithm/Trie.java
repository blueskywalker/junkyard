package algorithm;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.TreeMap;

/**
 * Created by jerrykim on 12/8/16.
 */
public class Trie {

    static class Node extends TreeMap<Character,Node> {
        private boolean terminated=false;

        public boolean isTerminated() {
            return terminated;
        }

        public void terminated() {
            this.terminated = true;
        }
    }

    public Trie() {

    }

    private Node root = new Node();

    public void add(String input) {
        Node node =root;

        for(Character c : input.toCharArray()) {
            if (!node.containsKey(c)) {
                node.put(c,new Node());
            }
            node=node.get(c);
        }
        node.terminated();
    }

    protected void traverse(Node node,StringBuilder sb) {
        int index = sb.length();
        if(node.isTerminated()) {
            System.out.println(sb.toString());
        }

        for(Character c: node.keySet()) {
            sb.append(c);
            traverse(node.get(c),sb);
            sb.deleteCharAt(index);
        }
    }

    public void list() {
        traverse(root,new StringBuilder());
    }

    public static void main(String[] args) {
        Trie trie = new Trie();

        trie.add("abcdef");
        trie.add("abcd");
        trie.add("abdef");
        trie.add("bcdef");

        trie.list();
    }
}
