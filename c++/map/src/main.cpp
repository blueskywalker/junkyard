
#include<iostream>
#include<map>


using namespace std;

class MyClass {
private:
  int _i;
public:
  MyClass() : _i(0) {}
  MyClass(int i) : _i(i) {}
  MyClass(const MyClass &) = default;
  int get() const { return _i; }

  bool operator<(const MyClass &other) {
    return _i < other._i;
  }

  friend ostream& operator<<(ostream& os, const MyClass& cls) {
    os << cls._i;
    return os;
  }
};


template<>
struct less<MyClass> {
  bool operator()(const MyClass &l, const MyClass &r) const {
    return l.get() < r.get();
  }
};

int main(int argc, char *argv[]) {

  map<MyClass, MyClass> hello;

  MyClass a(1);
  MyClass b(2);
  hello[a] = b;

  hello.insert(make_pair(MyClass(3), MyClass(4)));

  cout << hello[a] << endl;
  cout << hello[MyClass(3)] << endl;
  return 0;
}
