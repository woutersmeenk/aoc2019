def fft(signal):
    sig_len = len(signal)
    base_pattern = [0, 1, 0, -1]

    for phase in range(100):
        new_signal = []
        for offset in range(sig_len):
            new_elem = 0
            for i in range(offset, sig_len):
                pat_idx = ((i + 1) // (offset + 1)) % 4
                new_elem += signal[i] * base_pattern[pat_idx]
                # print(f"{signal[i]} * {base_pattern[pat_idx]} + ", end='')
            new_elem = abs(new_elem) % 10  # int(str(new_elem)[-1])
            new_signal.append(new_elem)
            # print(f"= {new_elem}")
        signal = new_signal
        #print(f"{phase}: {signal}")
        print(f"Phase {phase + 1}")
    return signal


if __name__ == "__main__":
    input_signal = open("16.dat", "r").readlines()[0].strip()
    signal = list(map(int, input_signal))

    signal = fft(signal)
    print(f"Part 1: {''.join(map(str,signal[0:8]))}")

    # signal = list(map(int, input_signal))

    # signal = fft(signal)
    # result_idx = int(input_signal[0:7])
    # print(f"Part 2: {''.join(map(str,signal[result_idx:result_idx+8]))}")
