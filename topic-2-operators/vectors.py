import struct
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fast_sqrt(x):
    # Fast inverse square root algorithm
    if x == 0:
        return 0.0

    threehalfs = 1.5
    x2 = x * 0.5
    y = x

    packed_y = struct.pack('f', y)
    i = struct.unpack('i', packed_y)[0]
    i = 0x5f3759df - (i >> 1)
    packed_i = struct.pack('i', i)
    y = struct.unpack('f', packed_i)[0]

    y = y * (threehalfs - (x2 * y * y))  # Newton-Raphson iteration

    return x * y  # sqrt(x) = x * (1/sqrt(x))

def normalize_vector_3d(v):
    """Normalize a 3D vector using fast sqrt."""
    x, y, z = v
    length_squared = x*x + y*y + z*z
    length = fast_sqrt(length_squared)
    return (x / length, y / length, z / length)

def multiple_a_vector_with_a_constant(v,constant):
    x, y, z = v
    return (x * constant, y * constant, z * constant)

def add_two_vectors(v1,v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return (x1+x2, y1+y2, z1+z2)

def draw_vectors_3d(v):
    """Draw the original and normalized 3D vectors."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Original vector (blue)
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', label='Original')
    # Normalized vector (red)
    normalized_v3d = normalize_vector_3d(v)
    ax.quiver(0, 0, 0, normalized_v3d[0], normalized_v3d[1], normalized_v3d[2], color='red', label='Normalized (Fast)')
    # Inverse of vector
    inverse_v3d = multiple_a_vector_with_a_constant(v,-1)
    ax.quiver(0, 0, 0, inverse_v3d[0], inverse_v3d[1], inverse_v3d[2], color='yellow', label='Inverse')
    # Add Normalized and Inverse vectors
    sum_of_inverse_and_normalized_vectors = add_two_vectors(inverse_v3d,normalized_v3d)
    ax.quiver(0, 0, 0, sum_of_inverse_and_normalized_vectors[0], sum_of_inverse_and_normalized_vectors[1], sum_of_inverse_and_normalized_vectors[2], color='orange', label='Inverse + Normalized')

    max_val = max(abs(val) for val in v + normalized_v3d)
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.title("3D Vectors")
    plt.savefig("vector_plot_3d.png")

# Example 3D vector
v3d = (3.0, 1.0, 2.0)
draw_vectors_3d(v3d)
