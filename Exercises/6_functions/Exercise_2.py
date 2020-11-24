def convert(exchangerate,euro):
    return euro * exchangerate


exchangerate = float(input('current dollar rate (€ > $): '))
euro = float(input('Your amount in euro: '))
print('€',euro,'=','$',convert(exchangerate,euro))