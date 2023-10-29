import streamlit as st

# 10進数を2進数に変換する関数
def decimal_to_binary(decimal):
    return bin(decimal)

# 10進数を16進数に変換する関数
def decimal_to_hex(decimal):
    return hex(decimal)

# Streamlitアプリのセットアップ
def main():
    st.title('10進数から2進数と16進数への変換')
    decimal_number = st.text_input('10進数を入力してください')
    
    if decimal_number:
        try:
            decimal_number = int(decimal_number)
            st.write(f'2進数: {decimal_to_binary(decimal_number)}')
            st.write(f'16進数: {decimal_to_hex(decimal_number)}')
        except ValueError:
            st.write('無効な入力です。数字を入力してください。')

if __name__ == '__main__':
    main()
