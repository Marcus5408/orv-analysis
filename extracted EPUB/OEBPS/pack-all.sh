#!/usr/bin/env bash
set -euo pipefail

if [[ ${1-} == "CI" ]]; then
	./scripts/pack-kieran.sh CI
else
	./scripts/pack-kieran.sh
fi

cd RAWs/RIP-Webnovel
zip -X -r "../../Omniscient Reader's Viewpoint - Sing-shong (singsyong)-clean.epub" mimetype OEBPS META-INF
cd ../..

# Naver fix for Apple Books
if [[ ${1-} == "CI" ]]; then
	sed -i 's,&nbsp;, ,g' RAWs/RIP-Naver/Vol*_Pt*/OEBPS/text/*.xhtml # Replace nbsp tags with a space
fi

# Deal with Vol1
for i in {1..8}; do
	# Copy shared files
	if [[ ${i} -ne 1 ]]; then
		cp -R RAWs/RIP-Naver/Vol1_Pt1/META-INF RAWs/RIP-Naver/Vol1_Pt${i}/
		cp -R RAWs/RIP-Naver/Vol1_Pt1/OEBPS/css RAWs/RIP-Naver/Vol1_Pt${i}/OEBPS/
		cp RAWs/RIP-Naver/Vol1_Pt1/OEBPS/*.ttf RAWs/RIP-Naver/Vol1_Pt${i}/OEBPS/
		cp RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/icon.png \
			RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/list_title.png \
			RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/pattern.png \
			RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/titlepage800.png \
			RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/munpia-logo.png \
			RAWs/RIP-Naver/Vol1_Pt${i}/OEBPS/images/
		cp RAWs/RIP-Naver/Vol1_Pt1/mimetype RAWs/RIP-Naver/Vol1_Pt${i}/
	fi
	cd RAWs/RIP-Naver/Vol1_Pt${i}
	zip -X -r "../../../Omniscient Reader's Viewpoint - Sing-shong (singsyong)-NaverVol1_Pt${i}.epub" mimetype OEBPS META-INF
	# Cleanup shared files
	if [[ ${i} -ne 1 ]]; then
		rm OEBPS/*.ttf
		rm -rf META-INF
		rm -rf OEBPS/css
		rm OEBPS/images/icon.png \
			OEBPS/images/list_title.png \
			OEBPS/images/pattern.png \
			OEBPS/images/titlepage800.png \
			OEBPS/images/munpia-logo.png
		rm mimetype
	fi
	cd -
done

# Deal with Vol2
for i in {1..4}; do
	# Copy shared files
	cp -R RAWs/RIP-Naver/Vol1_Pt1/META-INF RAWs/RIP-Naver/Vol2_Pt${i}/
	cp -R RAWs/RIP-Naver/Vol1_Pt1/OEBPS/css RAWs/RIP-Naver/Vol2_Pt${i}/OEBPS/
	cp RAWs/RIP-Naver/Vol1_Pt1/OEBPS/*.ttf RAWs/RIP-Naver/Vol2_Pt${i}/OEBPS/
	cp RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/icon.png \
		RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/list_title.png \
		RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/pattern.png \
		RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/titlepage800.png \
		RAWs/RIP-Naver/Vol1_Pt1/OEBPS/images/munpia-logo.png \
		RAWs/RIP-Naver/Vol2_Pt${i}/OEBPS/images/
	# Hack before we make a proper title page
	cp RAWs/unused-images/titlepage_v2.jpg RAWs/RIP-Naver/Vol2_Pt${i}/OEBPS/images/titlepage.jpg
	cp RAWs/RIP-Naver/Vol1_Pt1/mimetype RAWs/RIP-Naver/Vol2_Pt${i}/
	cd RAWs/RIP-Naver/Vol2_Pt${i}
	zip -X -r "../../../Omniscient Reader's Viewpoint - Sing-shong (singsyong)-NaverVol2_Pt${i}.epub" mimetype OEBPS META-INF
	# Cleanup shared files
	rm OEBPS/*.ttf
	rm -rf META-INF
	rm -rf OEBPS/css
	rm OEBPS/images/icon.png \
		OEBPS/images/list_title.png \
		OEBPS/images/pattern.png \
		OEBPS/images/titlepage800.png \
		OEBPS/images/munpia-logo.png
	# Hack before we make a proper title page
	rm OEBPS/images/titlepage.jpg
	rm mimetype
	cd -
done
