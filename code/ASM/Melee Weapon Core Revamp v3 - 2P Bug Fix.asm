# Inject @ 8009f260
## NEW VERSION
cmpwi r3, 5 # original
bne- exit # no melee weapon

# check for player1
lis r15, 0x807D
ori r15, r15, 0x71A0
lwz r16, 0x0(r15)
lwz r16, 0x0(r16)
lwz r22, 0x0004 (r31)
cmpw r16, r22
beq- p1 #player one confirmed
# check for p2 explicitly, because of partner struct
lwz r16, 0x8(r15)
# null check for partner (P3, P4 etc) or P2 not spawned
cmpwi r16, 0
beq- nullfail
# end null check
# check for player 2
lwz r16, 0x0(r16)
cmpw r16, r22
beq- p2 #player two confirmed

# NEW
bne- nullfail

p1:
lis r16, 0x8051 #junk mem
ori r16, r16, 0xA114 #junk mem
beq- checkByte

p2:
lis r16, 0x8051 #junk mem
ori r16, r16, 0xA115 #junk mem
#beq- checkByte (Implicit)

# check byte for mode
checkByte:
lbz r15, 0x0(r16)
cmpwi r15, 1
beq- exit #original melee desired
li r3, 9 # new melee desired, set r3 to result that triggers '0'
bne- exit # exit

nullfail:
cmpwi r3, 5

exit: