
#include <iostream>
#include <list>
#include <boost/any.hpp>

using boost::any_cast;
typedef std::list<boost::any> many;

void append_int(many & values, int value)
{
    boost::any to_append = value;
    values.push_back(to_append);
}

void append_string(many & values, const std::string & value)
{
    values.push_back(value);
}

void append_char_ptr(many & values, const char * value)
{
    values.push_back(value);
}

void append_any(many & values, const boost::any & value)
{
    values.push_back(value);
}

void append_nothing(many & values)
{
    values.push_back(boost::any());
}

int main(int argc,char *argv[])
{


	return 0;
}
