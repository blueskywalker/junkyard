package algorithm;

import java.util.HashMap;
import java.util.LinkedList;

/**
 * Created by jerrykim on 12/15/16.
 */
public class LRUCache<K,V> {

    public static class Node<K,V> {
        K key;
        V value;

        public Node(K key, V value) {
            this.key = key;
            this.value = value;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "key=" + key +
                    ", value=" + value +
                    '}';
        }
    }

    HashMap<K,Node> hash;
    LinkedList<Node> list;
    final int MAX;

    public LRUCache(int max) {
        hash = new HashMap<K, Node>();
        list = new LinkedList<>();

        MAX=max;
    }

    public synchronized void put(K key, V value) {
        if (!hash.containsKey(key)) {
            if (hash.size()>= MAX) {
                Node payload = list.removeFirst();
                hash.remove(payload);
            }
            Node newOne = new Node(key,value);
            hash.put(key,newOne);
            list.add(newOne);
        }
    }

    public synchronized V get(K key) {
        if (hash.containsKey(key)) {
            Node<K,V> payload = hash.get(key);
            list.remove(payload);
            list.add(payload);
            return payload.value;
        }
        return null;
    }

    @Override
    public String toString() {
        return "LRUCache{" +
                "list=" + list +
                '}';
    }

    public static void main(String[] args) {
        LRUCache<String,String> lru = new LRUCache<>(4);

        lru.put("a","aaa");
        lru.put("b","bbb");
        lru.put("c","ccc");
        lru.put("d","ddd");
        System.out.println(lru);
        lru.put("e","eee");
        System.out.println(lru);
        lru.get("c");
        System.out.println(lru);
    }

}
