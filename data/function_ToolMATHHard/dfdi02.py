def reduce_matrix_power_to_linear_combo(A, n: int):
    'Compute p,q such that A^n = p A + q I for a 2x2 matrix A.'
    if len(A) != 2 or any(len(row) != 2 for row in A):
        raise ValueError('A must be 2x2')
    tr = A[0][0] + A[1][1]
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    if n == 1:
        return [1, 0]
    if n == 2:
        return [tr, -det]
    # recurrence: A^k = tr A^{k-1} - det A^{k-2}
    u_prev, v_prev = tr, -det  # for k=2
    u_curr, v_curr = 1, 0       # for k=1
    for _k in range(3, n+1):
        u_next = tr*u_prev - det*u_curr
        v_next = tr*v_prev - det*v_curr
        u_curr, v_curr = u_prev, v_prev
        u_prev, v_prev = u_next, v_next
    return [u_prev, v_prev]
