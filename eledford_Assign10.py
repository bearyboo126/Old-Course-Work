#!/usr/bin/python3
# Name: Erin Ledford
# Class: BIOI 3500, Spring 2021
# Assignment #: Assignment 10
# Due Date: April 20th, 2021
#
# Honor Pledge: On my honor as a student of the University of Nebraska at
#               Omaha, I have neither given nor received unauthorized help on
#               this programming assignment.
#
# NAME: Erin Ledford
# EMAIL: eledford@unomaha.edu
#
# Partners: NONE
#
# This programming assignment computes and displays the frequency
# distribution of the amino acids from all the sequences in a given file,
# and that reports the sequence of id of the sequence with the lowest and
# highest amino acid content for each particular amino acid.

import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

class eledford_Assign10:
    def main():
        
        # Opens the human.1.protein.faa file to use a input
        fileIn = open('human.1.protein.faa', 'r')
        
        # Creates the eledford_results.txt file to store output
        fileOut = open('eledford_results.txt', 'w')
        
        # Finds the sequences and IDs of the input file 
        # and allows for parsing
        records = SeqIO.parse(fileIn, "fasta")
        
        # Keeps track of the highest A frequency distribution per sequence
        AFreqHigh = 0

        # Keeps track of the lowest A frequency distribution per sequence
        AFreqLow = 100

        # Keeps track of the amount of As in the input file
        ACounts = 0
        
        # Keeps track of the highest C frequency distribution per sequence
        CFreqHigh = 0

        # Keeps track of the lowest C frequency distribution per sequence
        CFreqLow = 100

        # Keeps track of the amount of Cs in the input file
        CCounts = 0
        
        # Keeps track of the highest D frequency distribution per sequence
        DFreqHigh = 0

        # Keeps track of the lowest D frequency distribution per sequence
        DFreqLow = 100

        # Keeps track of the amount of Ds in the input file
        DCounts = 0

        # Keeps track of the highest E frequency distribution per sequence
        EFreqHigh = 0

        # Keeps track of the lowest E frequency distribution per sequence
        EFreqLow = 100

        # Keeps track of the amount of Es in the input file
        ECounts = 0

        # Keeps track of the highest F frequency distribution per sequence
        FFreqHigh = 0

        # Keeps track of the lowest F frequency distribution per sequence
        FFreqLow = 100

        # Keeps track of the amount of Fs in the input file
        FCounts = 0

        # Keeps track of the highest G frequency distribution per sequence
        GFreqHigh = 0

        # Keeps track of the lowest G frequency distribution per sequence
        GFreqLow = 100

        # Keeps track of the amount of Gs in the input file
        GCounts = 0

        # Keeps track of the highest H frequency distribution per sequence
        HFreqHigh = 0

        # Keeps track of the lowest H frequency distribution per sequence
        HFreqLow = 100

        # Keeps track of the amount of Hs in the input file
        HCounts = 0

        # Keeps track of the highest I frequency distribution per sequence
        IFreqHigh = 0

        # Keeps track of the lowest I frequency distribution per sequence
        IFreqLow = 100

        # Keeps track of the amount of Is in the input file
        ICounts = 0

        # Keeps track of the highest K frequency distribution per sequence
        KFreqHigh = 0

        # Keeps track of the lowest K frequency distribution per sequence
        KFreqLow = 100

        # Keeps track of the amount of Ks in the input file
        KCounts = 0

        # Keeps track of the highest L frequency distribution per sequence
        LFreqHigh = 0

        # Keeps track of the lowest L frequency distribution per sequence
        LFreqLow = 100

        # Keeps track of the amount of Ls in the input file
        LCounts = 0

        # Keeps track of the highest M frequency distribution per sequence
        MFreqHigh = 0

        # Keeps track of the lowest M frequency distribution per sequence
        MFreqLow = 100

        # Keeps track of the amount of Ms in the input file
        MCounts = 0

        # Keeps track of the highest N frequency distribution per sequence
        NFreqHigh = 0

        # Keeps track of the lowest N frequency distribution per sequence
        NFreqLow = 100

        # Keeps track of the amount of Ns in the input file
        NCounts = 0

        # Keeps track of the highest P frequency distribution per sequence
        PFreqHigh = 0

        # Keeps track of the lowest P frequency distribution per sequence
        PFreqLow = 100

        # Keeps track of the amount of Ps in the input file
        PCounts = 0

        # Keeps track of the highest Q frequency distribution per sequence
        QFreqHigh = 0

        # Keeps track of the lowest Q frequency distribution per sequence
        QFreqLow = 100

        # Keeps track of the amount of Qs in the input file
        QCounts = 0

        # Keeps track of the highest R frequency distribution per sequence
        RFreqHigh = 0

        # Keeps track of the lowest R frequency distribution per sequence
        RFreqLow = 100

        # Keeps track of the amount of Rs in the input file
        RCounts = 0

        # Keeps track of the highest S frequency distribution per sequence
        SFreqHigh = 0

        # Keeps track of the lowest S frequency distribution per sequence
        SFreqLow = 100

        # Keeps track of the amount of Ss in the input file
        SCounts = 0

        # Keeps track of the highest T frequency distribution per sequence
        TFreqHigh = 0

        # Keeps track of the lowest T frequency distribution per sequence
        TFreqLow = 100

        # Keeps track of the amount of Ts in the input file
        TCounts = 0

        # Keeps track of the highest V frequency distribution per sequence
        VFreqHigh = 0

        # Keeps track of the lowest V frequency distribution per sequence
        VFreqLow = 100

        # Keeps track of the amount of Vs in the input file
        VCounts = 0

        # Keeps track of the highest W frequency distribution per sequence
        WFreqHigh = 0

        # Keeps track of the lowest W frequency distribution per sequence
        WFreqLow = 100

        # Keeps track of the amount of Ws in the input file
        WCounts = 0

        # Keeps track of the highest Y frequency distribution per sequence
        YFreqHigh = 0

        # Keeps track of the lowest Y frequency distribution per sequence
        YFreqLow = 100

        # Keeps track of the amount of Ys in the input file
        YCounts = 0
        
        # Counts all of the sequence lengths in the file
        recordLengths = 0

        # Parses through the file to find the count in each sequence of
        # each letter of amino acids and the frequency of each amino
        # acid in each sequence
        for record in records:
            # The sequence length is added to find the total
            # frequency distribution in the input file
            recordLengths += len(record)
            
            # The count of each amino acid for each sequence
            # used to find the total frequency distribution in the input file
            ACounts += record.seq.count('A')
            CCounts += record.seq.count('C')
            DCounts += record.seq.count('D')
            ECounts += record.seq.count('E')
            FCounts += record.seq.count('F')
            GCounts += record.seq.count('G')
            HCounts += record.seq.count('H')
            ICounts += record.seq.count('I')
            KCounts += record.seq.count('K')
            LCounts += record.seq.count('L')
            MCounts += record.seq.count('M')
            NCounts += record.seq.count('N')
            PCounts += record.seq.count('P')
            QCounts += record.seq.count('Q')
            RCounts += record.seq.count('R')
            SCounts += record.seq.count('S')
            TCounts += record.seq.count('T')
            VCounts += record.seq.count('V')
            WCounts += record.seq.count('W')
            YCounts += record.seq.count('Y')
            
            # The temporary frequency distribution of each
            # amino acid in the sequence which is used
            # to determine which sequence ID has the highest
            # and lowest frequency distribution
            AFreqTemp = record.seq.count('A') / len(record)
            CFreqTemp = record.seq.count('C') / len(record)
            DFreqTemp = record.seq.count('D') / len(record)
            EFreqTemp = record.seq.count('E') / len(record)
            FFreqTemp = record.seq.count('F') / len(record)
            GFreqTemp = record.seq.count('G') / len(record)
            HFreqTemp = record.seq.count('H') / len(record)
            IFreqTemp = record.seq.count('I') / len(record)
            KFreqTemp = record.seq.count('K') / len(record)
            LFreqTemp = record.seq.count('L') / len(record)
            MFreqTemp = record.seq.count('M') / len(record)
            NFreqTemp = record.seq.count('N') / len(record)
            PFreqTemp = record.seq.count('P') / len(record)
            QFreqTemp = record.seq.count('Q') / len(record)
            RFreqTemp = record.seq.count('R') / len(record)
            SFreqTemp = record.seq.count('S') / len(record)
            TFreqTemp = record.seq.count('T') / len(record)
            VFreqTemp = record.seq.count('V') / len(record)
            WFreqTemp = record.seq.count('W') / len(record)
            YFreqTemp = record.seq.count('Y') / len(record)

            # This section of code searches for the ID of the sequence for 
            # the highest and lowest frequency distribution by
            # using the temporary amino acid frequency to check and see if it
            # is the highest or lowest frequency of that amino acid.
            # If the sequence has the same highest or lowest frequency
            # distribution of a sequence that came before it
            # the code puts it into alphabetical order and uses the first one             #  as the lowest or highest ID
            if (AFreqTemp > AFreqHigh):
                AFreqHigh = AFreqTemp
                AFreqHighID = record.id
            if(AFreqTemp < AFreqLow):
                AFreqLow = AFreqTemp
                AFreqLowID = record.id
            if(AFreqTemp == AFreqHigh):
                if (record.id < AFreqHighID):
                    AFreqHighID = record.id
            if(AFreqTemp == AFreqLow):
                if (record.id < AFreqLowID):
                    AFreqLowID = record.id
            if (CFreqTemp > CFreqHigh):
                CFreqHigh = CFreqTemp
                CFreqHighID = record.id
            if (CFreqTemp < CFreqLow):
                CFreqLow = CFreqTemp
                CFreqLowID = record.id
            if (CFreqTemp == CFreqHigh):
                if (record.id < CFreqHighID):
                    CFreqHighID = record.id
            if (DFreqTemp > DFreqHigh):
                DFreqHigh = DFreqTemp
                DFreqHighID = record.id
            if (DFreqTemp < DFreqLow):
                DFreqLow = DFreqTemp
                DFreqLowID = record.id
            if (DFreqTemp == DFreqHigh):
                if (record.id < DFreqHighID):
                    DFreqHighID = record.id
            if (DFreqTemp == DFreqLow):
                if (record.id < DFreqLowID):
                    DFreqLowID = record.id
            if (EFreqTemp > EFreqHigh):
                EFreqHigh = EFreqTemp
                EFreqHighID = record.id
            if (EFreqTemp < EFreqLow):
                EFreqLow = EFreqTemp
                EFreqLowID = record.id
            if (EFreqTemp == EFreqHigh):
                if (record.id < EFreqHighID):
                    EFreqHighID = record.id
            if (EFreqTemp == EFreqLow):
                if (record.id < EFreqLowID):
                    EFreqLowID = record.id
            if (FFreqTemp > FFreqHigh):
                FFreqHigh = FFreqTemp
                FFreqHighID = record.id
            if (FFreqTemp < FFreqLow):
                FFreqLow = FFreqTemp
                FFreqLowID = record.id
            if (FFreqTemp == FFreqHigh):
                if(record.id < FFreqHighID):
                    FFreqHighID = record.id
            if (GFreqTemp > GFreqHigh):
                GFreqHigh = GFreqTemp
                GFreqHighID = record.id
            if (GFreqTemp < GFreqLow):
                GFreqLow = GFreqTemp
                GFreqLowID = record.id
            if (GFreqTemp == GFreqHigh):
                if (record.id < GFreqHighID):
                    GFreqHighID = record.id
            if (GFreqTemp == GFreqLow):
                if (record.id < GFreqLowID):
                    GFreqLowID = record.id
            if (HFreqTemp > HFreqHigh):
                HFreqHigh = HFreqTemp
                HFreqHighID = record.id
            if (HFreqTemp < HFreqLow):
                HFreqLow = HFreqTemp
                HFreqLowID = record.id
            if (HFreqTemp == HFreqHigh):
                if(record.id < HFreqHighID):
                    HFreqHighID = record.id
            if (HFreqTemp == HFreqLow):
                if (record.id < HFreqLowID):
                    HFreqLowID = record.id
            if (IFreqTemp > IFreqHigh):
                IFreqHigh = IFreqTemp
                IFreqHighID = record.id
            if (IFreqTemp < IFreqLow):
                IFreqLow = IFreqTemp
                IFreqLowID = record.id
            if(IFreqTemp == IFreqHigh):
                if (record.id < IFreqHighID):
                    IFreqHighID = record.id
            if (IFreqTemp == IFreqLow):
                if (record.id < IFreqLowID):
                    IFreqLowID = record.id
            if (KFreqTemp > KFreqHigh):
                KFreqHigh = KFreqTemp
                KFreqHighID = record.id
            if (KFreqTemp < KFreqLow):
                KFreqLow = KFreqTemp
                KFreqLowID = record.id
            if (KFreqTemp == KFreqHigh):
                if (record.id < KFreqHighID):
                    KFreqHighID = record.id
            if (KFreqTemp == KFreqLow):
                if (record.id < KFreqLowID):
                    KFreqLowID = record.id
            if (LFreqTemp > LFreqHigh):
                LFreqHigh = LFreqTemp
                LFreqHighID = record.id
            if (LFreqTemp < LFreqLow):
                LFreqLow = LFreqTemp
                LFreqLowID = record.id
            if (LFreqTemp == LFreqHigh):
                if (record.id < LFreqHighID):
                    LFreqHighID = record.id
            if (LFreqTemp == LFreqLow):
                if (record.id < LFreqLowID):
                    LFreqLowID = record.id
            if (MFreqTemp > MFreqHigh):
                MFreqHigh = MFreqTemp
                MFreqHighID = record.id
            if (MFreqTemp < MFreqLow):
                MFreqLow = MFreqTemp
                MFreqLowID = record.id
            if (MFreqTemp == MFreqHigh):
                if (record.id < MFreqHighID):
                    MFreqHighID = record.id
            if (MFreqTemp == MFreqLow):
                if (record.id < MFreqLowID):
                    MFreqLowID = record.id
            if (NFreqTemp > NFreqHigh):
                NFreqHigh = NFreqTemp
                NFreqHighID = record.id
            if (NFreqTemp < NFreqLow):
                NFreqLow = NFreqTemp
                NFreqLowID = record.id
            if (NFreqTemp == NFreqHigh):
                if (record.id < NFreqHighID):
                    NFreqHighID = record.id
            if (NFreqTemp == NFreqLow):
                if (record.id < NFreqLowID):
                    NFreqLowID = record.id
            if (PFreqTemp > PFreqHigh):
                PFreqHigh = PFreqTemp
                PFreqHighID = record.id
            if (PFreqTemp < PFreqLow):
                PFreqLow = PFreqTemp
                PFreqLowID = record.id
            if (PFreqTemp == PFreqHigh):
                if (record.id < PFreqHighID):
                    PFreqHighID = record.id
            if (PFreqTemp == PFreqLow):
                if (record.id < PFreqLowID):
                    PFreqLowID = record.id
            if (QFreqTemp > QFreqHigh):
                QFreqHigh = QFreqTemp
                QFreqHighID = record.id
            if (QFreqTemp < QFreqLow):
                QFreqLow = QFreqTemp
                QFreqLowID = record.id
            if (QFreqTemp == QFreqHigh):
                if (record.id < QFreqHighID):
                    QFreqHighID = record.id
            if (QFreqTemp == QFreqLow):
                if (record.id < QFreqLowID):
                    QFreqLowID = record.id
            if (RFreqTemp > RFreqHigh):
                RFreqHigh = RFreqTemp
                RFreqHighID = record.id
            if (RFreqTemp < RFreqLow):
                RFreqLow = RFreqTemp
                RFreqLowID = record.id
            if (RFreqTemp == RFreqHigh):
                if (record.id < RFreqHighID):
                    RFreqHighID = record.id
            if (RFreqTemp == RFreqLow):
                if (record.id < RFreqLowID):
                    RFreqLowID = record.id
            if (SFreqTemp > SFreqHigh):
                SFreqHigh = SFreqTemp
                SFreqHighID = record.id
            if (SFreqTemp < SFreqLow):
                SFreqLow = SFreqTemp
                SFreqLowID = record.id
            if (SFreqTemp == SFreqHigh):
                if (record.id < SFreqHighID):
                    SFreqHighID = record.id
            if (SFreqTemp == SFreqLow):
                if (record.id < SFreqLowID):
                    SFreqLowID = record.id
            if (TFreqTemp > TFreqHigh):
                TFreqHigh = TFreqTemp
                TFreqHighID = record.id
            if (TFreqTemp < TFreqLow):
                TFreqLow = TFreqTemp
                TFreqLowID = record.id
            if (TFreqTemp == TFreqHigh):
                if (record.id < TFreqHighID):
                    TFreqHighID = record.id
            if (TFreqTemp == TFreqLow):
                if (record.id < TFreqLowID):
                    TFreqLowID = record.id
            if (VFreqTemp > VFreqHigh):
                VFreqHigh = VFreqTemp
                VFreqHighID = record.id
            if (VFreqTemp < VFreqLow):
                VFreqLow = VFreqTemp
                VFreqLowID = record.id
            if (VFreqTemp == VFreqHigh):
                if (record.id < VFreqHighID):
                    VFreqHighID = record.id
            if (VFreqTemp == VFreqLow):
                if (record.id < VFreqLowID):
                    VFreqLowID = record.id
            if (WFreqTemp > WFreqHigh):
                WFreqHigh = WFreqTemp
                WFreqHighID = record.id
            if (WFreqTemp < WFreqLow):
                WFreqLow = WFreqTemp
                WFreqLowID = record.id
            if (WFreqTemp == WFreqHigh):
                if (record.id < WFreqHighID):
                    WFreqHigh = record.id
            if (WFreqTemp == WFreqLow):
                if (record.id < WFreqLowID):
                    WFreqLowID = record.id
            if (YFreqTemp > YFreqHigh):
                YFreqHigh = YFreqTemp
                YFreqHighID = record.id
            if (YFreqTemp < YFreqLow):
                YFreqLow = YFreqTemp
                YFreqLowID = record.id
            if (YFreqTemp == YFreqHigh):
                if (record.id < YFreqHighID):
                    YFreqHighID = record.id
            if (YFreqTemp == YFreqLow):
                if (record.id < YFreqLowID):
                    YFreqLowID = record.id

        # This section of code finds the frequency distribution for each
        # amino acid in the file
        AFreqsHigh = ACounts / recordLengths
        CFreqsHigh = CCounts / recordLengths
        DFreqsHigh = DCounts / recordLengths
        EFreqsHigh = ECounts / recordLengths
        FFreqsHigh = FCounts / recordLengths
        GFreqsHigh = GCounts / recordLengths
        HFreqsHigh = HCounts / recordLengths
        IFreqsHigh = ICounts / recordLengths
        KFreqsHigh = KCounts / recordLengths
        LFreqsHigh = LCounts / recordLengths
        MFreqsHigh = MCounts / recordLengths
        NFreqsHigh = NCounts / recordLengths
        PFreqsHigh = PCounts / recordLengths
        QFreqsHigh = QCounts / recordLengths
        RFreqsHigh = RCounts / recordLengths
        SFreqsHigh = SCounts / recordLengths
        TFreqsHigh = TCounts / recordLengths
        VFreqsHigh = VCounts / recordLengths
        WFreqsHigh = WCounts / recordLengths
        YFreqsHigh = YCounts / recordLengths

        # This section changes the frequency distribution into a percentage
        AFreqsHigh = AFreqsHigh * 100
        CFreqsHigh = CFreqsHigh * 100
        DFreqsHigh = DFreqsHigh * 100
        EFreqsHigh = EFreqsHigh * 100
        FFreqsHigh = FFreqsHigh * 100
        GFreqsHigh = GFreqsHigh * 100
        HFreqsHigh = HFreqsHigh * 100
        IFreqsHigh = IFreqsHigh * 100
        KFreqsHigh = KFreqsHigh * 100
        LFreqsHigh = LFreqsHigh * 100
        MFreqsHigh = MFreqsHigh * 100
        NFreqsHigh = NFreqsHigh * 100
        PFreqsHigh = PFreqsHigh * 100
        QFreqsHigh = QFreqsHigh * 100
        RFreqsHigh = RFreqsHigh * 100
        SFreqsHigh = SFreqsHigh * 100
        TFreqsHigh = TFreqsHigh * 100
        VFreqsHigh = VFreqsHigh * 100
        WFreqsHigh = WFreqsHigh * 100
        YFreqsHigh = YFreqsHigh * 100
        
        #This section of code formats the frequencies to two places after
        # the decimal point
        AFreqsHigh = '%.2f' % (AFreqsHigh)
        CFreqsHigh = '%.2f' % (CFreqsHigh)
        DFreqsHigh = '%.2f' % (DFreqsHigh)
        EFreqsHigh = '%.2f' % (EFreqsHigh)
        FFreqsHigh = '%.2f' % (FFreqsHigh)
        GFreqsHigh = '%.2f' % (GFreqsHigh)
        HFreqsHigh = '%.2f' % (HFreqsHigh)
        IFreqsHigh = '%.2f' % (IFreqsHigh)
        KFreqsHigh = '%.2f' % (KFreqsHigh)
        LFreqsHigh = '%.2f' % (LFreqsHigh)
        MFreqsHigh = '%.2f' % (MFreqsHigh)
        NFreqsHigh = '%.2f' % (NFreqsHigh)
        PFreqsHigh = '%.2f' % (PFreqsHigh)
        QFreqsHigh = '%.2f' % (QFreqsHigh)
        RFreqsHigh = '%.2f' % (RFreqsHigh)
        SFreqsHigh = '%.2f' % (SFreqsHigh)
        TFreqsHigh = '%.2f' % (TFreqsHigh)
        VFreqsHigh = '%.2f' % (VFreqsHigh)
        WFreqsHigh = '%.2f' % (WFreqsHigh)
        YFreqsHigh = '%.2f' % (YFreqsHigh)
        
        # This section of code creates the format for the output as described
        # in the assignment
        APrint = "A\t" + str(AFreqsHigh) + "%" + "\t" + AFreqLowID + "\t" + AFreqHighID + "\n"
        CPrint = "C\t" + str(CFreqsHigh) + "%" + "\t" + CFreqLowID + "\t" + CFreqHighID + "\n"
        DPrint = "D\t" + str(DFreqsHigh) + "%" + "\t" + DFreqLowID + "\t" + DFreqHighID + "\n"
        EPrint = "E\t" + str(EFreqsHigh) + "%" + "\t" + EFreqLowID + "\t" + EFreqHighID + "\n"
        FPrint = "F\t" + str(FFreqsHigh) + "%" + "\t" + FFreqLowID + "\t" + FFreqHighID + "\n"
        GPrint = "G\t" + str(GFreqsHigh) + "%" + "\t" + GFreqLowID + "\t" + GFreqHighID + "\n"
        HPrint = "H\t" + str(HFreqsHigh) + "%" + "\t" + HFreqLowID + "\t" + HFreqHighID + "\n"
        IPrint = "I\t" + str(IFreqsHigh) + "%" + "\t" + IFreqLowID + "\t" + IFreqHighID + "\n"
        KPrint ="K\t" + str(KFreqsHigh) + "%" + "\t" + KFreqLowID + "\t" + KFreqHighID + "\n"
        LPrint ="L\t" + str(LFreqsHigh) + "%" + "\t" + LFreqLowID + "\t" + LFreqHighID + "\n"
        MPrint ="M\t" + str(MFreqsHigh) + "%" + "\t" + MFreqLowID + "\t" + MFreqHighID + "\n"
        NPrint = "N\t" + str(NFreqsHigh) + "%" + "\t" + NFreqLowID + "\t" + NFreqHighID + "\n"
        PPrint ="P\t" + str(PFreqsHigh) + "%" + "\t" + PFreqLowID + "\t" + PFreqHighID + "\n"
        QPrint ="Q\t" + str(QFreqsHigh) + "%" + "\t" + QFreqLowID + "\t" + QFreqHighID + "\n"
        RPrint ="R\t" + str(RFreqsHigh) + "%" + "\t" + RFreqLowID + "\t" + RFreqHighID + "\n"
        SPrint ="S\t" + str(SFreqsHigh) + "%" + "\t" + SFreqLowID + "\t" + SFreqHighID + "\n"
        TPrint ="T\t" + str(TFreqsHigh) + "%" + "\t" + TFreqLowID + "\t" + TFreqHighID + "\n"
        VPrint ="V\t" + str(VFreqsHigh) + "%" + "\t" + VFreqLowID + "\t" + VFreqHighID + "\n"
        WPrint ="W\t" + str(WFreqsHigh) + "%" + "\t" + WFreqLowID + "\t" + WFreqHighID + "\n"
        YPrint ="Y\t" + str(WFreqsHigh) + "%" + "\t" + WFreqLowID + "\t" + WFreqHighID + "\n"
        
        # This section of code writes to the output file the formatted
        # strings for each amino acid frequency of the file
        fileOut.write(APrint)
        fileOut.write(CPrint)
        fileOut.write(DPrint)
        fileOut.write(EPrint)
        fileOut.write(FPrint)
        fileOut.write(GPrint)
        fileOut.write(HPrint)
        fileOut.write(IPrint)
        fileOut.write(KPrint)
        fileOut.write(LPrint)
        fileOut.write(MPrint)
        fileOut.write(NPrint)
        fileOut.write(PPrint)
        fileOut.write(QPrint)
        fileOut.write(RPrint)
        fileOut.write(SPrint)
        fileOut.write(TPrint)
        fileOut.write(VPrint)
        fileOut.write(WPrint)
        fileOut.write(YPrint)
        
        # Closes the input file
        fileIn.close()

        # Closes the output file
        fileOut.close()

    if __name__ == '__main__':
        main()
