Inject @ 800A1518

# Check which player
lis r15, 0x807D
ori r15, r15, 0x71A0
lwz r16, 0x0 (r15)
lwz r16, 0x0 (r16)
lwz r16, 0x224(r16)
addi r22, r31, 0x4
lwz r22, 0x0(r22)
lwz r22, 0x224(r22)
cmpw r16, r22
beq- checkState # (P1)

checkP2:
addi r15, r15, 0x8
lwz r16, 0x0(r15)
lwz r16, 0x0(r16)
lwz r16, 0x224(r16)
cmpw r16, r22
bne- end # Partner case

checkState:
# Get player behavior state
lwz r16, 0x0 (r15)
lwz r16, 0x0 (r16)
lwz r16, 0x22C (r16)
lwz r16, 0x30 (r16)
lwz r16, 0x10 (r16)

compareState:
cmpwi r16, 6 #jumpdash
beq- allowLightDash
cmpwi r16, 9 #homingjump
beq- allowLightDash
cmpwi r16, 23 #skydive
beq- allowLightDash
bne- end

allowLightDash:
lis r15, 0x800A
ori r15, r15, 0x1520
mtlr r15
blr

end:
li r3, 0


------------

# Inject @ 8008A498

# Check which player
lis r15, 0x807D
ori r15, r15, 0x71A0
lwz r16, 0x0 (r15)
lwz r16, 0x0 (r16)
lwz r16, 0x224(r16)
addi r22, r31, 0x4
lwz r22, 0x0(r22)
lwz r22, 0x224(r22)
cmpw r16, r22
beq- checkState # (P1)

checkP2:
addi r15, r15, 0x8
lwz r16, 0x0(r15)
lwz r16, 0x0(r16)
lwz r16, 0x224(r16)
cmpw r16, r22
bne- end # Partner case

checkState:
# Get player behavior state
lwz r16, 0x0 (r15)
lwz r16, 0x0 (r16)
lwz r16, 0x22C (r16)
lwz r16, 0x30 (r16)
lwz r16, 0x10 (r16)

compareState:
cmpwi r16, 6 #jumpdash
beq- allowLightDash
cmpwi r16, 9 #homingjump
beq- allowLightDash
cmpwi r16, 23 #skydive
beq- allowLightDash
bne- end

allowLightDash:
lis r15, 0x8008
ori r15, r15, 0xA4A0
mtlr r15
blr

end:
li r3, 0