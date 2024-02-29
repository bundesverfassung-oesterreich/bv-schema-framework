B-VG: Erste Fragen zu den Editionsrichtlinien

Bisher lässt sich festhalten, dass wir beschlossen haben, Zeilen und Seiten nicht wie in den edierten Dokumenten darzustellen, also die Seiten/Zeilen der Dokumente nicht visuell zu imitieren. Des Weiteren bin ich – nach den bisherigen Absprachen – davon ausgegangen, dass wir anstreben, möglichst Texte zu bieten, die als Fließtext auch gut rezipiert werden können. Da es sich bei den meisten Dokumenten, mit den wir arbeiten (seien es Verfassungsentwürfe, seien es Protokolle), um Dokumente handelt, die Dritte adressieren, ist aus pragmatischen Gründen in ihnen die Tendenz zu einer gut rezipierbaren, finalen ›Schicht‹ bereits angelegt und auch klar erkennbar.

Ich habe hier eine sortierte Liste von Phänomenen erstellt, die wir theoretisch kodiert erfassen könnten. Es ist in jedem Fall vor allem zu überlegen, ob dies einen besonderen Nutzen auf Seiten der Rezeption birg. Zudem sollte berücksichtigt werden, dass eventuell kaum qualifiziertes Personal zur Verfügung stehen wird, um die editorischen Entscheidungen und Analysen zu vollziehen, die jede dieser Kodierungen im Einzelfall voraussetzt. Ich habe die folgende Kategorisierung bloß vorgenommen, um alles etwas übersichtlicher zu gestalten und einmal alles, was denkbar wäre, aufzuzählen. Damit ist nicht gesagt, dass sich die Dinge, die hier aufgezählt werden, auch allesamt umsetzen lassen. Es geht also erst einmal darum, Wünsche und Anforderungen zu konkretisieren; über die konkrete, technische Realisierbarkeit kann erst zu einem fortgeschrittenerem Zeitpunkt entschieden werden.

## Materielle Dimension

Sollen konkrete Schreibwerkzeuge auf Ebener kleinerer textueller Einheiten erfasst werden? (Z.B. Das Wort »aber« wurde mit Blei hinzugefügt.)

```xml
<handShift medium="plombium"/>aber<handShift medium="default"/>
```

Sollen verschiedene Urheber auf Ebener kleinerer textueller Einheiten erfasst werden? (Z.B. Das Wort »aber« wurde von Renner hinzugefügt.)

```xml
<handShift medium="plombium" scribeRef="bv_id_123"/>aber<handShift medium="default"/>
```

Sollen Einklebungen (vgl .z.B. Renner 1918) auf Ebene der spezifischen textuellen Einheit erfasst werden?

```xml
<add type="eingeklebt" hand="#bv_id_123">
   <p>Österreich ist eine demokratische Republik. Ihr
      <lb break="yes"/>Recht geht vom Volk aus.
      </p>
</add>
```

Sollen Hervorhebungen spezifisch erfasst werden? Sollen also verschiedene Unterstreichungen differenziert werden? Sollen Typenwechsel als solche erfasst werden oder reicht es, ihre generelle funktionale Dimension (z.B. Hervorhebung) zu kodieren?

```xml
<p>
      <hi rend="emphasis">Entwurf</hi>
      <lb break="yes"/><hi rend="emphasis">einer österreichischen Verfassung</hi>
      <lb break="yes"/><hi rend="emphasis">beschlossen von den am 18. und 19. April 1920 in Linz versammelten</hi>
      <lb break="yes"/><hi rend="emphasis">Vertretern der nationalen Partei- und Landes-Organisationen.</hi>
      <lb break="yes"/>Unter dem Zwange des Vertrages von St. Germain, der
      <lb break="yes"/>den Anschluß an das Deutsche Reich derzeit verwehrt, in dem
      <lb break="yes"/>Bestreben, dem bedrängten Volke des deutschen Alpenlandes den
      <lb break="yes"/>Aufstieg zu ermöglichen, schließen sich die geschichtlich gewordenen
      <lb break="yes"/>selbständigen Länder Niederöstereich, Oberösterreich, Salzburg,
      <lb break="yes"/>Steiermark, Kärnten, Tirol und Vorarlberg zu einem Bundesstaat
      <lb break="yes"/>sich nachstehende Verfassung:
      <lb break="yes"/>zusammen und geben
      <lb break="yes"/><hi rend="emphasis">l. Hauptteil.</hi>
      <lb break="yes"/><hi rend="emphasis">Aufbau und Aufgaben des Staates.</hi>
</p>
<p>
      <hi rend="emphasis">Entwurf</hi>
      <lb break="yes"/><hi rend="bold">einer österreichischen Verfassung</hi>
      <lb break="yes"/><hi rend="bold">beschlossen von den am 18. und 19. April 1920 in Linz versammelten</hi>
      <lb break="yes"/><hi rend="bold">Vertretern der nationalen Partei- und Landes-Organisationen.</hi>
      <lb break="yes"/>Unter dem Zwange des Vertrages von St. Germain, der
      <lb break="yes"/>den Anschluß an das Deutsche Reich derzeit verwehrt, in dem
      <lb break="yes"/>Bestreben, dem bedrängten Volke des deutschen Alpenlandes den
      <lb break="yes"/>Aufstieg zu ermöglichen, schließen sich die geschichtlich gewordenen
      <lb break="yes"/>selbständigen Länder Niederöstereich, Oberösterreich, Salzburg,
      <lb break="yes"/>Steiermark, Kärnten, Tirol und Vorarlberg zu einem Bundesstaat
      <lb break="yes"/>sich nachstehende Verfassung:
      <lb break="yes"/>zusammen und geben
      <lb break="yes"/><hi rend="bold">l. Hauptteil.</hi>
      <lb break="yes"/><hi rend="bold">Aufbau und Aufgaben des Staates.</hi>
</p>
```

## Spatiale Dimension

Soll der Ort, an dem sich etwa eine Einfügung befindet, erfasst werden?

https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.placement.html

```xml
<add place="margin">[An addition written in the margin]</add>
<add place="bottom opposite">[An addition written at the
 foot of the current page and also on the facing page]</add>
```

Sollen spatiale/typografische Eigenschaften z.B. von Kolumnen etc. erfasst werden? (Ich würde davon abraten, da die Vorteile sehr gering, die Probleme für die online Darstellung relativ groß sind.)
```
<cb/>Text einer Kolumne<cb/>Text der nächsten Kolumne
```
Mimetische Darstellung im Web-Layout technisch nicht möglich.

## Genetische/Temporale Dimension

Sollen Streichungen kodiert werden?
```
<del hand="#bv_id_124">gestrichen</del>
```

Sollen Ersetzungen kodiert werden? Sollen Überschreibung kodiert werden? (Oder reicht es etwa, sie als Streichung und Einfügung zu kodieren?)
Genetisches Geschehen:
```xml
<p> Der Gesetzgebung des Bundes <restore hand="#bv_id_9889">
    <subst>
        <del hand="#bv_id_123">wird übertragen:</del>
        <add place="margin" hand="#bv_id_678">kommen zu:</add>
    </subst>
</restore>
</p>
```

```xml
   Etwas wurde 
   <restore hand="#bv_id_123">
         <del hand="#bv_id_222">gestrichen</del>
   </restore> aber dann auch wieder nicht.
```

Sollen Sofortänderung von späterer Überarbeitung durch Kodierungen unterschieden werden?
Wenn innerhalb eines Dokuments globale genetische Vorgänge definiert und identifiziert werden können, empfielt sich die Kodierung über `<handNote>` Elemente, die die einzelnen abgeschlossenen Bearbeitungsschritte beschreiben und referenzierbar machen.

## Intertextuelle Dimension

Sollen Referenzen auf externe Texte kodiert werden?
```xml
    <rs type="bibl" ref="zotero_id_xyz123"></rs>
    <rs type="bibl" ref="http://wichtige-juristische-quelle.at"></rs>
```
Wie sollen Referenzen auf interne Dokumente verlinkt werden?
```xml
    wie der werte Kollege bereits in seinem <rs type="bv_text" ref="#bv_doc_id_123|bv_element_id_123">Entwurf</rs> feststellt
```

Sollen Identitätsverhältnisse von Textteilen kodiert werden? (Z.B. ›Artikel 1 in Entwurf Y entspricht Artikel 200 in Entwurf Z.‹)
```xml
    <note type="editor">Absatz entspricht <rs type="bv_text" ref="#bv_doc_id_123|bv_element_id_123">Kelsen I</rs></note>
```


## Metatextuelle Dimension

Sollen im Dokument existierende historische Kommentare so kodiert werden, dass ihr Bezugspunkt im ›Fließtext‹ erfasst wird? Beispiel: metatextueller Kommentar am Rand: "Sehr richtig!!"

```xml
    <anchor type="hist" xml:id="a_1222_s"/>
    der souveränen Länder
    <note type="hist" xml:id="a_1222_e" hand="#bv_id_1234lksdjf">
        Sehr richtig!!
    </note>
```

Paginierungen. Sollen die existierenden Paginierungen erfasst werden oder reichen die von uns auf Grundlage des Bildwechsels erzeugten?

```xml
<lb break="yes"/>gesetzwidrigen Vollzugsanweisung und verpflich<ab type="pagination">80</ab><pb facs="#facs_55" n="55" xml:id="img_0055" break="no"/><ab type="pagination">- 54 -</ab>tet die erlassende Behörde zur Kundmachung der</p>
```

Folierungen. Ein Gleiches.

Lebende/tote Kolumnentitel. Müssen diese konkret erfasst werden, oder reicht z.B. eine Beschreibung/Anmerkung im editorischen Kommentar?

```xml
<fw type="column_title">Ein Kolumenentitel</fw>
<p>Beginn des Seitentextes …</p>
```

Fortsetzungszeichen (Z.B. »./.«) bei Seitenwechseln im Absatz. Müssen diese dem Medium des Typoskripts geschuldeten Zeichen erhalten werden? Einziger relevanter Grund scheinen hypothetische Fälle zu sein, in denen ein Fehlen Textverluste wahrscheinlich macht. Das kann aber leichter durch Kommentierung erschlossen werden.

## Kommentare der Herausgeber.

Erfolgen diese mit direktem Stellenbezug im Rahmen des edierten Dokumentes und/oder verweist nur ein externer Fließtext (editorischer Kommentar) auf spezifische Stellen im Text?

```xml
    <p>
        Die Republik Deutschösterreich ist ein freier Bund <anchor type="editor" xml:id="a_1222_s"/> der souveränen Länder 
        <note type="editor" xml:id="a_1222_e">
            <rs ref="p_0001" type="person">Kelsen</rs> am Rand: <note type="original">Artikel?</note>; aus: <del>souveräner Länder</del>
        </note> ; Sie besteht aus neun selbstständigen Bundesländern. 
    </p>
```

Wie komplex sind die Kommentare der Herausgeber gestaltet? Besteht hier die Notwendigkeit neben Referenzen auf ›Stellen‹ / Texte / Quellen z.B. auch Streichungen zu erfassen?

Normalisierungen/Eingriffe.  
Sind orthographische Normalisierungen angezeigt? Falls ja: Sollen die Originalzustände dennoch konserviert werden? (Bitte zu bedenken, dass z.B. sprachistorische Forschungen von originalen Graphien profitieren könnten und das Normalisieren zugleich mit einigem Zeitaufwand verbunden ist.)
