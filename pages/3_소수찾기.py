import streamlit as st
import math

st.title("에라토스테네스의 체 (Sieve of Eratosthenes)")

st.write("""
에라토스테네스의 체는 주어진 숫자 이하의 모든 소수를 찾는 고대 알고리즘입니다.
""")

# 사용자 입력
n = st.number_input("최대값을 입력하세요 (2 이상):", min_value=2, max_value=1000, value=30, step=1)

col1, col2 = st.columns(2)

with col1:
    if st.button("알고리즘 실행", use_container_width=True):
        st.session_state.run_algorithm = True

with col2:
    if st.button("초기화", use_container_width=True):
        st.session_state.run_algorithm = False

# 알고리즘 실행
if st.session_state.get("run_algorithm", False):
    st.divider()
    st.subheader("단계별 실행 과정")
    
    # 배열 초기화
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    steps = []
    crossed_out_numbers = set()
    
    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            step_info = {
                'current': i,
                'crossed': list(crossed_out_numbers),
                'description': f"숫자 {i}의 배수를 제거합니다 ({i}는 소수입니다)"
            }
            steps.append(step_info)
            
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                crossed_out_numbers.add(j)
    
    # 단계별 시각화
    for idx, step in enumerate(steps):
        st.write(f"**단계 {idx + 1}: {step['description']}**")
        
        # 현재 상태의 숫자 표시
        display_text = ""
        for num in range(2, n + 1):
            if num in step['crossed']:
                display_text += f"~~{num}~~ "
            elif num == step['current']:
                display_text += f"**{num}** "
            elif is_prime[num]:
                display_text += f"{num} "
            else:
                display_text += f"~~{num}~~ "
        
        st.write(display_text)
        st.write("")
    
    # 최종 결과
    st.divider()
    st.subheader("최종 결과")
    
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    
    st.success(f"**{n}까지의 소수: {len(primes)}개**")
    st.write(primes)

st.divider()
st.subheader("알고리즘 설명")
st.write("""
1. **초기화**: 2부터 n까지 모든 수를 소수로 표시합니다.
2. **반복**: 
   - 현재 수 i가 소수라면, i의 모든 배수를 합성수로 표시합니다.
   - √n까지만 반복하면 됩니다.
3. **결과**: 표시되지 않은 모든 수가 소수입니다.

**시간복잡도**: O(n log log n)
""")
