import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    """n의 제곱수로 2 dimentional array를 생성하는 ndarray.
    Args:
        n: the real part (default 0.0)
        dtype: 생성하려는 ndarray의 data type (np.int)
    Returns:
        row와 column의 길이가 n인 two dimentional ndarray로
        X[0,0]은 0으로 순차적으로 X[n-1,n-1]은 n^2이 할다됨
    """

    X = np.arange(n*n, dtype=dtype).reshape(n, -1)
    return X


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    """shape이 지정된 크기의 ndarray를 생성.
    이때 행렬의 element는 type에 따라 0, 1 또는 empty로 생성됨
    Args:
        shape: 생성할려는 ndarray의 shape
        type: 생성되는 element들의 값을 지정함0은 0, 1은 1, 99는 empty 타입으로 생성됨
        dtype: 생성하려는 ndarray의 data type (np.int)
    Returns:
        shape의 크기로 생성된 ndarray로 type에 따라 element의 내용이 변경됨
    Examples:
        >>> zero_or_one_or_empty_ndarray(shape=(2,2), type=1)
        array([[ 1,  1],
               [ 1,  1]])
        >>> zero_or_one_or_empty_ndarray(shape=(3,3), type=99) #임의의수 생성
        array([[1773984320,        487, 1774114944],
               [       487, 1947927088,          0],
               [1947927088,          0, 1701605485]])
    """
    if type == 0:
        X = np.zeros(shape, dtype)
    elif type == 1:
        X = np.ones(shape, dtype)
    else:
        X = np.empty(shape, dtype)

    return X


def change_shape_of_ndarray(X, n_row):
    """입력된 ndarray X를 n_row를 고려하여 matrix로 반환함.
    - 이때 입력하는 X의 size는 2의 거듭제곱수로 전제함.
    - 만약 n_row과 1일 때는 matrix가 아닌 vector로 반환함.
    Args:
        X: 입력하는 ndarray
        n_row: 생성할려는 matrix의 row의 개수
    Returns:
        row의 개수가 n_row인 Matrix 또는 Vector
    Examples:
        >>> import numpy as np
        >>> import numpy_lab as testcode
        >>> X = np.ones((32,32), dtype=np.int)
        >>> testcode.change_shape_of_ndarray(X, 1)
        array([1, 1, 1, ..., 1, 1, 1])
        >>> testcode.change_shape_of_ndarray(X, 512)
        array([[1, 1],
               [1, 1],
               [1, 1],
               ...,
               [1, 1],
               [1, 1],
               [1, 1]])
    """
    if n_row == 1:
        return X.flatten()
    else:
        return X.reshape(n_row, -1)

def concat_ndarray(X_1, X_2, axis):
    """입력된 ndarray X_1과 X_2를 axis로 입력된 축을 기준으로 통합하여 반환하는 함수
    - X_1과 X_2는 matrix 또는 vector 임, 그러므로 vector 일 경우도 처리할 수 가 있어야 함
    - axis를 기준으로 통합할 때, 통합이 불가능하면 False가 반환됨.
    - 단 X_1과 X_2 Matrix, Vector 형태로 들어왔다면, Vector를 row가 1개인
      Matrix로 변환하여 통합이 가능한지 확인할 것
    Args:
        X_1: 입력하는 ndarray
        X_2: 입력하는 ndarray
        axis: 통합의 기준이 되는 축 0 또는 1임
    Returns:
        X_1과 X_2과 통합된 matrix 타입의 ndarray
    Examples:
        >>> import numpy as np
        >>> import numpy_lab as testcode
        >>> a = np.array([[1, 2], [3, 4]])
        >>> b = np.array([[5, 6]])
        >>> testcode.concat_ndarray(a, b, 0)
        array([[1, 2],
               [3, 4],
               [5, 6]])
        >>> testcode.concat_ndarray(a, b, 1)
        False
        >>> a = np.array([1, 2])
        >>> b = np.array([5, 6, 7])
        >>> testcode.concat_ndarray(a, b, 1)
        array([[1, 2, 5, 6, 7]])
        >>> testcode.concat_ndarray(a, b, 0)
        False
    """
    try:
        if X_1.ndim == 1:
            X_1 = X_1.reshape(1, -1)
        if X_2.ndim == 1:
            X_2 = X_2.reshape(1, -1)
        return np.concatenate((X_1, X_2), axis=axis)
    except ValueError as e:
        return False


def normalize_ndarray(X, axis=99, dtype=np.float32):
    """입력된 Matrix 또는 Vector를 ndarray X의 정규화된 값으로 변환하여 반환함
    - 이때 정규화 변환 공식 `Z = (X - X의평균) / X의 표준편차`로 구성됨.
    - X의 평균과 표준편차는 axis를 기준으로 axis 별로 산출됨.
    - Matrix의 경우 axis가 0 또는 1일 경우, row 또는 column별로 Z value를 산출함.
    - axis가 99일 경우 전체 값에 대한 normalize 값을 구함.
    Args:
        X: 입력하는 ndarray,
        axis: normalize를 구하는 기준이 되는 축으로 0, 1 또는 99임
              단 99는 axis 구분 없이 전체값으로 평균과 표준편차를 구함
        dtype: data type으로 np.float32로 구정
    Returns:
        정규화된 ndarray
    Examples:
        >>> import numpy as np
        >>> import numpy_lab as testcode
        >>> X = np.arange(12, dtype=np.float32).reshape(6,2)
        >>> testcode.normalize_ndarray(X)
        array([[-1.59325504, -1.3035723 ],
               [-1.01388955, -0.72420681],
               [-0.43452409, -0.14484136],
               [ 0.14484136,  0.43452409],
               [ 0.72420681,  1.01388955],
               [ 1.3035723 ,  1.59325504]], dtype=float32)
        >>> testcode.normalize_ndarray(X, 1)
        array([[-1.,  1.],
               [-1.,  1.],
               [-1.,  1.],
               [-1.,  1.],
               [-1.,  1.],
               [-1.,  1.]], dtype=float32)
        >>> testcode.normalize_ndarray(X, 0)
        array([[-1.46385002, -1.46385002],
               [-0.87831002, -0.87831002],
               [-0.29277   , -0.29277   ],
               [ 0.29277   ,  0.29277   ],
               [ 0.87831002,  0.87831002],
               [ 1.46385002,  1.46385002]], dtype=float32)
    """
    X = X.astype(np.float32)
    n_row, n_column = X.shape
    if axis == 99:
        x_mean = np.mean(X)
        x_std = np.std(X)
        Z = (X - x_mean) / x_std
    if axis == 0:
        x_mean = np.mean(X, 0).reshape(1, -1)
        x_std = np.std(X, 0).reshape(1, -1)
        Z = (X - x_mean) / x_std
    if axis == 1:
        x_mean = np.mean(X, 1).reshape(n_row, -1)
        x_std = np.std(X, 1).reshape(n_row, -1)
        Z = (X - x_mean) / x_std

    return Z


def save_ndarray(X, filename="test.npy"):
    """입력된 ndarray X를 argument filename으로 저장함
    Args:
        X: 입력하는 ndarray
        filename: 저장할려는 파일네임
    Examples:
        >>> import numpy as np
        >>> import numpy_lab as testcode
        >>> X = np.arange(32, dtype=np.float32).reshape(4, -1)
        >>> filename = "test.npy"
        >>> testcode.save_ndarray(X, filename) #test.npy 파일이 생성됨
    """

    f = open(filename, "wb")
    np.save(f, X)
    f.close()


def boolean_index(X, condition):
    """입력된 ndarray X를 String type의 condition 정보를 바탕으로 해당 컨디션에 해당하는
       ndarray X의 index 번호를 반환함
    Args:
        X: 입력하는 ndarray
        condition: string type의 조건 (">3", "== 5", "< 15")
    Examples:
        >>> import numpy as np
        >>> import numpy_lab as testcode
        >>> X = np.arange(32, dtype=np.float32).reshape(4, -1)
        >>> testcode.boolean_index(X, "== 3")
        (array([0]), array([3]))
        >>> X = np.arange(32, dtype=np.float32)
        >>> testcode.boolean_index(X, "> 6")
        (array([ 7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                23, 24, 25, 26, 27, 28, 29, 30, 31]),)
    """
    condition = eval(str("X") + condition)
    return np.where(condition)

def find_nearest_value(X, target_value):
    """입력된 vector type의 ndarray X에서 target_value와 가장 차이가 작게나는 element를
       찾아 리턴함 이때 X를 list로 변경하여 처리하는 것은 실패로 간주함.
    Args:
        X: 입력하는 vector type의 ndarray
        target_value : 가장 유사한 값의 기준값이 되는 값
    Return:
        target_value와 가장 유사한 값
    Examples:
        >>> import numpy as np
        >>> import numpy_lab as testcode
        >>> X = np.random.uniform(0, 1, 100)
        >>> target_value = 0.3
        >>> testcode.find_nearest_value(X, target_value)
        0.29260674329282488 # 출력되는 값은 random 하게 바뀜
    """

    result = X[np.argmin(np.abs(X - target_value))]
    return result

def get_n_largest_values(X, n):
    """입력된 vector type의 ndarray X에서 큰 숫자 순서대로 n개의 값을 반환함.
    Args:
        X : vector type의 ndarray
        n : 반환할려는 element의 개수
    Return:
        ndarray X의 element중 큰 숫자 순서대로 n개 값이 반환됨 ndarray
    Examples:
    >>> import numpy as np
    >>> import numpy_lab_solution as t
    >>> X = np.random.uniform(0, 1, 100)
    >>> t.get_n_largest_values(X, 3)
    array([ 0.98935239,  0.98494578,  0.98317255])
    >>> t.get_n_largest_values(X, 5)
    array([ 0.98935239,  0.98494578,  0.98317255,  0.96859596,  0.96485649])
    # 출력되는 값은 random 하게 바뀜
    """

    X_expected = X[np.argsort(X)[-n:]][::-1]
    return X_expected
