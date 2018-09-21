
#include<iostream>
#include<map>


using namespace std;

class MyClass {
private:
  int _i;
public:
  MyClass(int i) : _i(i) {}
  int get() const { return _i; }

  bool operator<(const MyClass &other) {
    return _i < other._i;
  }
};


template<>
struct less<MyClass> {
  bool operator()(const MyClass &l, const MyClass &r) const {
    return l.get() < r.get();
  }
};

int main(int argc, char *argv[]) {

  map<MyClass, int> hello;

  MyClass a(1);
  hello[a] = 10;

  return 0;
}
