datatype Tree<T> = Leaf | Node(Tree<T>, Tree<T>, T)
datatype List<T> = Nil | Cons(T, List<T>)

function flatten<T>(tree:Tree<T>):List<T>
{
    match tree
    case Leaf => Nil
    case Node(ta,tb,n) => append(flatten(ta), Cons(n,flatten(tb)))

}

function append<T>(xs:List<T>, ys:List<T>):List<T>
{
	match xs
    case Nil => ys
    case Cons(first, rest) => Cons(first, append(rest, ys))

}

function treeContains<T>(tree:Tree<T>, element:T):bool
{
	match tree
    case Leaf => false
    case Node(ta,tb,x) => element == x || treeContains(ta,element) || treeContains(tb, element)
}

function listContains<T>(xs:List<T>, element:T):bool
{
	match xs
    case Nil => false
    case Cons(y,ys') => element == y || listContains(ys',element)
    
}

ghost method elementOfAppend<T>(xs:List<T>, ys:List<T>, element:T)
ensures listContains(append(xs, ys), element) <==> listContains(xs, element) || listContains(ys, element)
{
    match(xs)
        case Nil => {
            assert listContains(append(xs, ys), element)
                == listContains(ys, element)
                == false || listContains(ys, element)
                == listContains(xs, element) || listContains(ys, element);
        }
        case Cons(x, xs') => {
            elementOfAppend(xs', ys, element);

            assert listContains(append(xs, ys), element)
                == listContains(append(Cons(x, xs'), ys), element)
                == listContains(Cons(x, append(xs', ys)), element)
                == (element == x || listContains(append(xs', ys), element));
        }
}

lemma sameElements<T>(tree:Tree<T>, element:T)
ensures treeContains(tree, element) <==> listContains(flatten(tree), element)
{
	match(tree)
        case Leaf => {
            assert treeContains(Leaf, element) 
                == false
                == listContains(Nil, element)
                == listContains(flatten(Leaf), element);
        }
        case Node(ta, tb, n) => {
            sameElements(ta, element);
            sameElements(tb, element);
            elementOfAppend(Cons(n, flatten(ta)), flatten(tb), element);

            assert treeContains(Node(ta, tb, n), element)
                == (element == n || treeContains(ta, element) || treeContains(tb, element))
                == (element == n || listContains(flatten(ta), element) || listContains(flatten(tb), element));
            
            assert listContains(flatten(tree), element)
                == listContains(append(flatten(ta), Cons(n, flatten(tb))), element)
                == (listContains(Cons(n, flatten(ta)), element)|| listContains(flatten(tb), element))
                == (element == n || listContains(flatten(ta), element) || listContains(flatten(tb), element));
        }
}