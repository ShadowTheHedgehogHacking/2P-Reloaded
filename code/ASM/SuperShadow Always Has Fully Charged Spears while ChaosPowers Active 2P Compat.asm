Inject @ 802F0D20
lis r15, 0x8057
ori r15, r15, 0x66D0
lwz r16, 0x0(r15)
cmpwi r16, 1
bge- ChaosPowered
addi r15, r15, 0xC
lwz r16, 0x0(r15)
cmpwi r16, 1
bge- ChaosPowered
# no chaos powers
lfs f1, 0x007C (r28)
bne- end

ChaosPowered:
lfs f1, -0x0338(r2)

end:


Inject @ 802F0D94 (audio tier 1)
lis r15, 0x8057
ori r15, r15, 0x66D0
lwz r16, 0x0(r15)
cmpwi r16, 1
bge- ChaosPowered
addi r15, r15, 0xC
lwz r16, 0x0(r15)
cmpwi r16, 1
bge- ChaosPowered
fmr f31, f0
#no chaos powers
bne- end

ChaosPowered:
nop #replace in McM with b 0x802F0DC0

end:


Inject @ 802F0FFC
lis r15, 0x8057
ori r15, r15, 0x66D0
lwz r16, 0x0(r15)
cmpwi r16, 1
bge- ChaosPowered
addi r15, r15, 0xC
lwz r16, 0x0(r15)
cmpwi r16, 1
bge- ChaosPowered
li r0, 1
#no chaos powers
bne- end

ChaosPowered:
nop #replace in McM with b 0x802F1018

end: