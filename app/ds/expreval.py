"""Infix, prefix and postfix expressions.

Computers need to know exactly what operators to perform and in what order.
One way to write an expression that guarantees there will be no confusion wrt
the order of operations is to create a fully parenthesized expression. This
type of expression uses one pair of parentheses for each operator. There is no
need to remember any precedence rules.

Infix expression   Prefix expression   Postfix expression
A + B              + A B               A B +
(A + B) * C        * + A B C           A B + C *

Operators are no longer ambiguous wrt the operands that they work on in prefix
and postfix. Only infix notation requires the additional symbols. The order of
operations within prefix and postfix expressions is completely determined by
the position of the operator and nothing else. In many ways, this makes infix
the least desirable notation to use.

The position of the parenthesis pair in infix expressions are clues to
the final position of the enclosed operator. If the operator were
moved to its corresponding right parenthesis position and the matching
left parenthesis were removed, the postfix would result. If we do the
same thing but we move the operator to the left parenthesis instead,
the prefix would result.
"""

from __future__ import division, print_function

__all__ = ["ExprEval"]
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-26'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-25'
__version__ = '1.2'  # Support **

import sys
sys.path.append('../../')
from algds.ds.stack import Stack


class ExprEval(object):
    """Convert infix expression to postfix expression and evalutate the result.

    Attributes:
        _operators (set): Valid operators
        _prec (dict of (str, int)): Holds the precedence values for the
            operators. "(" will receive the lowest value possible.

    >>> expr_eval = ExprEval()
    >>> expr_eval.infix2postfix('A * B + C * D')
    'A B * C D * +'
    >>> expr_eval.infix2postfix('( A + B ) * ( C + D )')
    'A B + C D + *'
    >>> expr_eval.infix2postfix('( A + B ) * C')
    'A B + C *'
    >>> expr_eval.infix2postfix('A + B * C')
    'A B C * +'
    >>> expr_eval.infix2postfix('5 * 3 ** ( 4 - 2 )')
    '5 3 4 2 - ** *'
    >>> expr_eval.eval('4 5 6 * +')
    34.0
    >>> expr_eval.eval('7 8 + 3 2 + /')
    3.0
    >>> expr_eval.eval('5 3 4 2 - ** *')
    45.0
    """

    def __init__(self):
        self._operators = {'+', '-', '*', '/', '**'}
        self._prec = {}
        self._prec['**'] = 4
        self._prec['*'] = 3
        self._prec['/'] = 3
        self._prec['+'] = 2
        self._prec['-'] = 2
        self._prec['('] = 1

    def infix2postfix(self, infix_expr):
        """Convert any infix expression to a postfix expression.

        For example, A + B * C -> A B C * +. The operands stay in their
        relative positions. It is only the operators that change position.
        The order of the operators in the original expression may be reversed
        in the resulting postfix expression due to their precedence.

        Another example, (A + B) * C -> A B + C *. When we see a left
        parenthesis, we will save it to denote that another operator of high
        precedence will be coming. When that right parenthesis does appear,
        the operator can be popped from the stack.

        Args:
            infix_expr (str): Infix expression where tokens are delimited by
                spaces. The operator tokens are *, /, +, -, (, and ). The
                operand tokens are the single-character identifiers A, B, C,
                etc.

        Returns:
            (str): Posfix expression.

        Raises:
            ValueError: If unknown character in infix_expr is found.
        """
        stack = Stack()  # Keep operators
        post_expr = []   # For output
        for ch in infix_expr.split():
            if ch.isupper() or ch.isdigit():  # ch is an operand
                post_expr.append(ch)
            elif ch == '(':
                stack.push(ch)
            elif ch == ')':
                # Pop the stack until the corresponding "(" is removed.
                # Append each operator to the end of the output list.
                top = stack.pop()
                while top != '(':
                    post_expr.append(top)
                    top = stack.pop()
            elif ch in self._operators:
                # First remove any operators already in the stack that have
                # higher or equal precedence and append them to the output list.
                while (not stack.isEmpty() and
                       self._prec[stack.top()] >= self._prec[ch]):
                    post_expr.append(stack.pop())
                # Then push the current character in the stack.
                stack.push(ch)
            else:
                raise ValueError('Unkown character %s' % ch)

        # Any operators still on the stack can be removed and appended to the
        # end of the output list.
        while not stack.isEmpty():
            post_expr.append(stack.pop())

        return ' '.join(post_expr)

    def eval(self, post_expr):
        """Evaluate an postfix expression.

        Whenever an operator is seen on the input, the two most recent operands
        will be used in the evaluation. So a stack is again the data structure
        of choice. When the final operator is processed, there will be only one
        value left on the stack. Pop and return it as the result of the
        expression.

        Args:
            post_expr (str): A postfix expression of tokens delimited by spaces.
                The operators are *, /, +, and -, and the operands are assumed
                to be single-digit integer values.

        Returns:
            (float): The evalutation result.

        Raises:
            ValueError: If unknown character in post_expr is found.
        """
        stack = Stack()
        for ch in post_expr.split():
            if ch.isdigit():             # ch is an operand
                stack.push(int(ch))
            elif ch in self._operators:  # ch is an operator
                # Be careful: the first pop is the second operand, and the
                # second pop is the first operand.
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self._operator_result(ch, operand1, operand2)
                stack.push(result)
            else:
                raise ValueError('Unkown character %s in the argument' % ch)
        # When the input expression has been completely processed, the result
        # is in the stack.
        return float(stack.pop())

    def _operator_result(self, operator, operand1, operand2):
        """Helper function to peform +-*/ arithmetic operation.

        Note that the operands in the postfix expression are in their original
        order.  When the operands are popped from the stack, they are reversed.
        This affect the operators which are not commutative.

        Args:
            operator (str '+-*/')
            operand1 (int/float)
            operand1 (int/float)

        Returns:
            (int/float): Arithmetic result.
        """
        if operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '**':
            return operand1 ** operand2
        else:
            raise ValueError('Unkown operator %s' % operator)


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
