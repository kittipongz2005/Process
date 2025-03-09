import multiprocessing
import time
import random


def is_prime(n):
    """ตรวจสอบว่า n เป็นจำนวนเฉพาะหรือไม่"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def check_prime_parallel(numbers):
    """ใช้ Process Pool เพื่อตรวจสอบจำนวนเฉพาะแบบขนาน"""
    with multiprocessing.Pool() as pool:
        results = pool.map(is_prime, numbers)
    return results


def check_prime_sequential(numbers):
    """ตรวจสอบจำนวนเฉพาะทีละตัวตามลำดับ"""
    results = [is_prime(n) for n in numbers]
    return results


if __name__ == "__main__":
    # สร้างชุดตัวเลขสุ่มสำหรับทดสอบ
    numbers = [random.randint(10**10, 10**11) for _ in range(10000)]

    # วัดเวลาการทำงานแบบ Parallel
    print("Starting parallel prime number check")
    start = time.time()
    parallel_results = check_prime_parallel(numbers)
    parallel_duration = time.time() - start
    print(f"Parallel duration: {parallel_duration:.4f} seconds")

    # วัดเวลาการทำงานแบบ Sequential
    print("Starting sequential prime number check")
    start = time.time()
    sequential_results = check_prime_sequential(numbers)
    sequential_duration = time.time() - start
    print(f"Sequential duration: {sequential_duration:.4f} seconds")

    # เปรียบเทียบผลลัพธ์
    print(
        f"\nParallel is {sequential_duration / parallel_duration:.2f}x faster than sequential"
    )
