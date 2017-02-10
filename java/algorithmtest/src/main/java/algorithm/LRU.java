package algorithm;

import java.util.HashMap;

/**
 * Created by jerrykim on 12/15/16.
 */
public class LRU {

    public static interface Cache<K,V> {
        public void put(K key,V value);
        public V get(K key);
    }

    public static class PayLoad<K,V> {
        K key;
        V value;

        public PayLoad(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "key=" + key +
                    ", value=" + value +
                    '}';
        }
    }

    public static class Node<K,V> {
        Node prev;
        Node next;
        PayLoad<K,V> payload;

        public Node(PayLoad<K, V> payload) {
            this.payload = payload;
            this.prev=null;
            this.next=null;
        }

        public PayLoad<K, V> getPayload() {
            return payload;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "payload=" + payload +
                    '}';
        }
    }

    public static class DoubleLinkedList<K,V> {
        Node<K,V> head;
        Node<K,V> tail;

        public DoubleLinkedList() {
            head=null;
            tail=null;
        }

        public void append(Node node) {
            if(head==null) {
                head=node;
                tail=node;
            } else {
                node.next = head;
                head.prev = node;
                head = node;
            }
        }

        public Node pop() {
            if (tail!=null) {
                Node node = tail;
                node.prev.next=null;
                tail = node.prev;
                node.prev=null;
                node.next=null;
                return node;
            }

            return null;
        }

        public void deleteAt(Node node) {
            if (node!=null) {
                if(node.prev != null)
                    node.prev.next=node.next;
                if(node.next != null)
                    node.next.prev=node.prev;
            }
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            for(Node node=head;node!=null;node=node.next) {
                sb.append(node);
                if(node.next!=null) {
                    sb.append("\n");
                }
            }
            return sb.toString();
        }
    }

    public static class LRUCache<K,V> implements  Cache<K,V> {
        final int MAX;

        HashMap<K,Node<K,V>> hash;
        DoubleLinkedList<K,V> list;

        public LRUCache(int max) {
            MAX=max;
            hash = new HashMap<K, Node<K,V>>();
            list = new DoubleLinkedList<K, V>();
        }

        @Override
        public void put(K key, V value) {
            if(! hash.containsKey(key)) {
                if (hash.size() >= MAX) {
                    list.pop();
                    hash.remove(key);
                }
                Node<K,V> node = new Node<K,V>(new PayLoad<K,V>(key,value));
                hash.put(key,node);
                list.append(node);
            }
        }

        @Override
        public V get(K key) {
            if (hash.containsKey(key)) {
                Node<K,V> node = hash.get(key);
                list.deleteAt(node);
                list.append(node);
                return node.getPayload().value;
            }
            return null;
        }

        @Override
        public String toString() {
            return "LRUCache{" +
                    "list=" + list +
                    '}';
        }
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
    }
}
