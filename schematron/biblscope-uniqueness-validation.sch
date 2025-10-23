<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron" 
        xmlns:tei="http://www.tei-c.org/ns/1.0"
        queryBinding="xslt2">
    
    <title>BV Project: biblScope Uniqueness Validation</title>
    
    <ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
    
    <pattern id="biblscope-uniqueness">
        <title>Check biblScope[@unit='part'] uniqueness across files in same dataset</title>
        
        <rule context="tei:TEI">
            <!-- Get the dataset ID of the current document -->
            <let name="current-dataset" value="normalize-space(.//tei:idno[@type='bv_data_set'])"/>
            
            <!-- Get the biblScope part value of the current document -->
            <let name="current-part" value="normalize-space(.//tei:seriesStmt/tei:biblScope[@unit='part'])"/>
            
            <!-- Get the directory of the current file -->
            <let name="base-dir" value="replace(base-uri(/), '[^/]+$', '')"/>
            
            <!-- Load all XML files in the same directory -->
            <let name="all-files" value="collection(concat($base-dir, '?select=*.xml;recurse=no'))"/>
            
            <!-- Filter files that belong to the same dataset -->
            <let name="same-dataset-files" value="$all-files[.//tei:idno[@type='bv_data_set' and normalize-space() = $current-dataset]]"/>
            
            <!-- Get all biblScope part values from files in the same dataset -->
            <let name="all-parts" value="for $doc in $same-dataset-files 
                                        return normalize-space($doc//tei:seriesStmt/tei:biblScope[@unit='part'])"/>
            
            <!-- Count how many times the current part value appears -->
            <let name="part-count" value="count($all-parts[. = $current-part])"/>
            
            <!-- Ensure the current document has a dataset ID -->
            <assert test="$current-dataset != ''">
                This document must have a bv_data_set idno to validate biblScope uniqueness.
            </assert>
            
            <!-- Ensure the current document has a biblScope part value -->
            <assert test="$current-part != ''">
                This document must have a biblScope[@unit='part'] value in seriesStmt.
            </assert>
            
            <!-- Check uniqueness -->
            <assert test="$part-count = 1">
                biblScope[@unit='part'] value "<value-of select="$current-part"/>" is not unique in dataset "<value-of select="$current-dataset"/>". 
                Found <value-of select="$part-count"/> occurrences across files in the same dataset.
                Each document in a dataset must have a unique biblScope[@unit='part'] value.
            </assert>
            
            <!-- Verify that seriesStmt title matches the dataset -->
            <assert test="normalize-space(.//tei:seriesStmt/tei:title) = $current-dataset">
                seriesStmt/title ("<value-of select="normalize-space(.//tei:seriesStmt/tei:title)"/>") should match the bv_data_set idno ("<value-of select="$current-dataset"/>").
            </assert>
        </rule>
    </pattern>
    
</schema>