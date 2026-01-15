# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        num_to_index = {num: i for i, num in enumerate(preorder)}
        nodes_no_parent_found = []

        def construct_left_subtree(query_position: int) -> TreeNode | None:
            """
            スタック `nodes_to_parent_found` には、左部分木はできているが、
            親と右部分木が分かっていないノードが生成された順に積まれている。
            `preorder` で `query_position` に位置するノードをクエリとして、
            このノードの左部分木をスタックにあるノードから構築する。
            なお、inorder順でノードを生成してスタックに積んでいるので、
            クエリノードの左部分木に含まれるであろうノードはすべてスタックに存在する。
            """
            child = None

            while nodes_no_parent_found:
                node = nodes_no_parent_found[-1]

                # preorderは、根→左→右の走査順であることから、
                # preorder上で後に登場する ⇔ より深い層に存在する
                deeper_than_query = query_position < num_to_index[node.val]
                if deeper_than_query:
                    nodes_no_parent_found.pop()
                    node.right = child
                    child = node
                else:
                    break

            return child

        for value in inorder:
            node = TreeNode(value)
            node_position = num_to_index[node.val]
            node.left = construct_left_subtree(node_position)
            nodes_no_parent_found.append(node)

        # preorderの最左端のさらに左（番兵）を指定することで
        # スタックに残ったノードを回収する
        return construct_left_subtree(-1)
