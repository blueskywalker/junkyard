

def build_tree(preorder):
    if len(preorder) < 2:
        return preorder

    head, tail = preorder[0], preorder[1:]
    left = [ item for item in tail if item < head]
    right = tail[len(left):]
    return [build_tree(left), head, build_tree(right)]

def main():
    data = [5, 2, 1, 3, 7]
    print(build_tree(data))

if __name__ == "__main__":
    main()